import streamlit as st
from PIL import Image
from PIL.ImageFilter import *
st.markdown("<h1 style='text-align:center;'>Image Editor</h1>",unsafe_allow_html=True)
st.markdown("---")
image=st.file_uploader("Upload image", type=["jpg","jpeg","png"])
info=st.empty()
size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    st.image(image)
    # print(img)
    # print(img.mode)
    # print(img.format)
    # print(img.size)
    info.markdown("<h2 style='text-align:center;'>Info</h2>",unsafe_allow_html=True)    
    size.markdown(f"<h6>Size: {img.size}</h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>mode: {img.mode}</h6>",unsafe_allow_html=True)

    st.markdown("<h2 style='text-align:center;'>Resize</h2>",unsafe_allow_html=True)    
    width=st.number_input("Width", value=img.width)
    height=st.number_input("Height", value=img.height)
    st.markdown("<h2 style='text-align:center;'>Rotation</h2>",unsafe_allow_html=True)    
    degree=st.number_input("Degree")
    st.markdown("<h2 style='text-align:center;'>Filters</h2>",unsafe_allow_html=True)    
    filters=st.selectbox("Filters", options=("None", "Blur", "Detail","Emboss", "Smooth"))
    btn_state=st.button("Submit")
    if btn_state:
        edited=img.resize((width, height)).rotate(degree)
        # st.image(edited)
        filtered=edited
        if filters != "None":
            if filters=="Blur":
                filtered=edited.filter(BLUR)
            elif filters=="Detail":
                filtered=edited.filter(DETAIL)
            elif filters=="Emboss":
                filtered=edited.filter(EMBOSS)
            elif filters=="Smooth":
                filtered=edited.filter(SMOOTH)
        st.image(filtered)