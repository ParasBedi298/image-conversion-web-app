import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
import io
from parts.instructions import instructions_page
from parts.sideb import sb
from parts.submitted import submitted_uploads_page
from parts.compare import compare_images

# Page Config
st.set_page_config(page_title="HistologyNet", page_icon="📋", initial_sidebar_state="expanded")

# Session-State Variables
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = None
    st.rerun()

# Some Functions
def basic_uploads_page():
    uploaded_files = st.file_uploader("Upload image(s) for segmentation here:", type=["jpg", "png"], accept_multiple_files=True)
    if uploaded_files:
        st.session_state.uploaded_files = uploaded_files
    st.text("")

    _, _, btn1, btn2 = st.columns(4)

    if btn1.button("Enhance/Edit Images", help = "Crop/Rotate the input images before segmentation"):
        if st.session_state.uploaded_files is None:
            st.warning("Please select at least one image file to proceed.")
        else:
            st.session_state.page = "enhance_uploads"
            st.rerun()
    if btn2.button("Submit for Segmentation", help = "Directly submit the images to segmentation model"):
        if st.session_state.uploaded_files is None:
            st.warning("Please select at least one image file to proceed.")
        else:
            st.session_state.page = "submitted_uploads"
            st.rerun()

    st.markdown("***")
    st.write("Uploaded Images:")
    cols=st.columns(4)

    if (st.session_state.uploaded_files):
        for i,uploaded_file in enumerate(st.session_state.uploaded_files):
                try:
                    image_data = uploaded_file.read()
                    img = Image.open(io.BytesIO(image_data))
                    cols[i%4].image(img,caption=uploaded_file.name, use_column_width=True)
                    # st.image(img, caption=uploaded_file.name, use_column_width=False)
                except Exception as e:
                    st.error(f"Error processing {uploaded_file.name}:{e}")

def enhance_uploads_page():
    st.write("That will come from Shashank's code :) But for now just displaying the images as it is")

    cols=st.columns(4)
    if (st.session_state.uploaded_files):
        for i,uploaded_file in enumerate(st.session_state.uploaded_files):
                try:
                    image_data = uploaded_file.read()
                    img = Image.open(io.BytesIO(image_data))
                    cols[i%4].image(img,width=150,caption=uploaded_file.name)
                    # st.image(img, caption=uploaded_file.name, use_column_width=False)
                except Exception as e:
                    st.error(f"Error processing {uploaded_file.name}:{e}")

    _, _, _, btn2 = st.columns(4)
    if btn2.button("Submit for Segmentation", help = "Click here to submit these images to the model"):
        st.session_state.page = 'submitted_uploads'
        st.rerun()

# Side Bar
sb()

# Main Content Begins
st.title("HistologyNet")
st.markdown('''##### <span style="color:gray">Self-Supervised Segmentation Masking for Histology Images</span>
            ''', unsafe_allow_html=True)

tab_instr, tab_upload = st.tabs(["Instructions", "Upload"])

#-----------------
# Instructions Tab
#-----------------

with tab_instr:
    instructions_page()
    
#-----------------
# Upload Tab
#-----------------

with tab_upload:
    if 'page' not in st.session_state:
        st.session_state.page = "basic_uploads"
        st.rerun()

    if st.session_state.page == "basic_uploads":
        basic_uploads_page()

    elif st.session_state.page == "enhance_uploads":
        enhance_uploads_page()

    elif st.session_state.page == "submitted_uploads":
        submitted_uploads_page(st.session_state.uploaded_files)

    elif st.session_state.page == "compare_uploads":
        compare_images()

    
