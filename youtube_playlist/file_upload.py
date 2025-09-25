import streamlit as st
st.title("FILE UPLOAD")
image= st.file_uploader("Please upload an image", type=["png", "jpg", "jpeg"])
if image is not None:
    st.image(image)

video= st.file_uploader("Please upload an video", type="mp4")
if video is not None:
    st.video(video)


images= st.file_uploader("Please upload images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)