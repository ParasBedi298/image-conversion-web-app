import streamlit as st

def sb():
    col1, col2, col3 = st.sidebar.columns([1,8,1])
    with col1:
        st.write("")
    with col2:
        st.image('statics/sample_image.png',  use_column_width=True)
    with col3:
        st.write("")

    st.sidebar.markdown(" ## About HistologyNet")
    st.sidebar.markdown("Bla-bla-bla: Revolutionize biomedical image segmentation by harnessing the power of self-supervised learning. A self-supervised learning model for efficient binary segmentation of histology images, without the need for extensive manual annotation"  )              
    st.sidebar.info("Read more about how the model works and see the code on [Github](https://github.com).", icon="ℹ️")