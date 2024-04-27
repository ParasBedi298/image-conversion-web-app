import streamlit
from streamlit_image_comparison import image_comparison

def compare_images(uploaded_files, segmented_files):
    for i in range(len(uploaded_files)):
        image_comparison(
            uploaded_files[i],
            segmented_files[i],
            label1 = "Original",
            label2 = "Masked"
        )