import streamlit as st
from streamlit_image_comparison import image_comparison
from PIL import Image
import io

def submitted_uploads_page(files):
    
    if st.button("Upload New Files"):
        st.session_state.page = "basic_uploads"
        st.session_state.uploaded_files = None
        st.rerun()

    st.write("Segmentation Results: ")
    st.write("")

    cols = st.columns(3)
    with cols[0]:
        st.markdown("<p style='text-align: center;'>Original Image</p>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<p style='text-align: center;'>Segmentation</p>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown("<p style='text-align: center;'>Comparison</p>", unsafe_allow_html=True)

    for uploaded_file in files:
        try:
            # Display original image in the first column
            with cols[0]:
                image_data = uploaded_file.read()
                img = Image.open(io.BytesIO(image_data))
                st.image(img, use_column_width=True)
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")

        try:
            # Display masked image in the second column
            with cols[1]:
                gray = img.convert('L')
                st.image(gray, use_column_width=True)
        except Exception as e:
            st.error(f"Error processing {gray.name}: {e}")

        # Display image comparison in the third column
        with cols[2]:
            # Resize original and masked images to a fixed size for comparison
            image_comparison(
                img1=img,
                img2=gray,
                label1="Original",
                label2="Masked",
                width=225
            )


# import streamlit as st
# from streamlit_image_comparison import image_comparison
# from PIL import Image
# import io

# def resize_image(image, target_size):
#     """Resize the image to match the target size while maintaining the aspect ratio."""
#     return image.resize(target_size, Image.BILINEAR)

# def final_display(uploaded_files, segmented_files):
#     cols = st.columns(3)
#     with cols[0]:
#         st.header("Original Images")
#     with cols[1]:
#         st.header("Segmentation Mask")
#     with cols[2]:
#         st.header("Compare images")
#     for uploaded_file, segmented_file in zip(uploaded_files, segmented_files):
#         try:
#             # Display original image in the first column
#             with cols[0]:
#                 image_data = uploaded_file.read()
#                 img = Image.open(io.BytesIO(image_data))
#                 st.image(img, caption=uploaded_file.name, use_column_width=True)
#         except Exception as e:
#             st.error(f"Error processing {uploaded_file.name}: {e}")

#         try:
#             # Display masked image in the second column
#             with cols[1]:
#                 mask_data = segmented_file.read()
#                 mask = Image.open(io.BytesIO(mask_data))
#                 st.image(mask, caption=segmented_file.name, use_column_width=True)
#         except Exception as e:
#             st.error(f"Error processing {segmented_file.name}: {e}")

#         # Display image comparison in the third column
#         with cols[2]:
#             # Resize original and masked images to a fixed size for comparison
#             img_resized = resize_image(img, (800, 800))
#             mask_resized = resize_image(mask, (800, 800))
#             image_comparison(
#                 img1=img_resized,
#                 img2=mask_resized,
#                 label1="Original",
#                 label2="Masked",
#                 width = 225
#             )

# def main():
#     uploaded_files = st.file_uploader("Upload image(s) for segmentation here:", type=["jpg", "png"], accept_multiple_files=True)
#     segmented_files = st.file_uploader("Upload segmented image(s) here:", type=["jpg", "png"], accept_multiple_files=True)
#     if uploaded_files and segmented_files:
#         final_display(uploaded_files, segmented_files)

# if __name__ == '__main__':
#     main()
        