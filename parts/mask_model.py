import ternausnet
import ternausnet.models
import numpy as np
from PIL import Image
import io

import torch
from torch import nn
from torchvision import transforms
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.optim import Adam
import matplotlib.pyplot as plt


def load_model(path, device='cpu'): # Check for GPU or CPU
    x = ternausnet.models.UNet11(pretrained=True) 
    model = x
    optimizer = Adam(model.parameters(), lr=0.001)
    checkpoint = torch.load(path, map_location=torch.device(device))
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    model = model.to(device)

    return model


def get_masked_image(uploaded_file, model, device='cpu'): # Check for GPU or CPU
    image_data = uploaded_file.read()
    input_image = Image.open(io.BytesIO(image_data))
    if input_image.mode != 'RGB':
        input_image = Image.merge("RGB", (input_image, input_image, input_image))
    transform = transforms.Compose([
        transforms.ToTensor(),  # resizing may be needed
    ])
    input_tensor = transform(input_image).unsqueeze(0).to(device)

    model.eval()  
    with torch.no_grad():
        output_tensor = model(input_tensor)
        output_tensor = torch.sigmoid(output_tensor)
    output_numpy = output_tensor.squeeze().cpu().numpy() # Check for GPU or CPU
    output_numpy = (output_numpy > 0.5).astype(np.uint8)
    output_image = Image.fromarray(output_numpy * 255)

    return output_image


# model = load_model('../model/model_2.pth')
# input_image_path = '../statics/sample_image.png'
# output_image = get_output_image(input_image_path, model)
# output_image.save('../statics/masked_sample_image.jpg')


def mask_images(uploaded_files, checkpoint_path, device):
    segmented_files = []
    model = load_model(checkpoint_path, device)
    for uploaded_file in uploaded_files:
        segmented_file = get_masked_image(uploaded_file, model, device)
        segmented_files.append(segmented_file)
    return segmented_files