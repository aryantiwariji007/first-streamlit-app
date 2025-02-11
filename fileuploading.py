import pandas as pd
import streamlit as st
from PIL import Image
st.title('File Uploading')
#1.Image
st.subheader('1.Uploading the Image')
img_file=st.file_uploader('Upload image',type=['png','jpeg','jpg'])
if img_file is not None:
    

    file_details={'file_name':img_file.name,'file_type':img_file.type,'file_size':img_file.size}
    st.write(file_details)
    st.image(Image.open(img_file))

#2.Audio

st.subheader('2.Uploading an audio')
img_file=st.file_uploader('Upload Audio',type=['wav','mp3'])
if img_file is not None:
    

    file_details={'file_name':img_file.name,'file_type':img_file.type,'file_size':img_file.size}
    st.write(img_file)
    st.audio(img_file)
#Video

st.subheader('3.Uploading video')
img_file=st.file_uploader('Upload Video',type=['mov','mp4'])
if img_file is not None:
    

    file_details={'file_name':img_file.name,'file_type':img_file.type,'file_size':img_file.size}
    st.write(img_file)
    st.video(img_file)

#csv

st.subheader('4.Uploading csv file')
img_file=st.file_uploader('Upload csv file',type=['csv'])
if img_file is not None:
    

    file_details={'file_name':img_file.name,'file_type':img_file.type,'file_size':img_file.size}
    st.write(img_file)
    st.image(Image.open(img_file))
