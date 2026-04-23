# License: MIT
# Author: Omar Alkousa
# Email: omar.ok1998@gmail.com
# LinkedIn: linkedin.com/in/omar-alkousa/
# Medium: medium.com/@omar.ok1998


# Import the required package
import streamlit as st
from skimage.io import imread
import global_thresholding
import local_thresholding
import manual_thresholding

# Sembunyikan tombol Deploy dan menu
css = '''
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none !important;}
    a[href^="https://"] {text-decoration: none;}
    a[href^="https://"]::after {content: none !important;}
    .stApp {
        background: linear-gradient(135deg, #1E90FF 0%, #FFFFFF 100%);
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

#################
# Documentation #
#################
# Set a title of the app
st.markdown("<h1 style='text-align: center; color: white;'>Thresholding Medical Images",
            unsafe_allow_html=True)


###################
# Upload an image #
###################
uploaded_file = st.file_uploader(label="Unggah file gambar")

# If the file is uploaded
if uploaded_file is not None:

    # Caching the data for faster implementation
    @st.cache_data
    def load_image():
        img = imread(fname=uploaded_file.name, as_gray=True)
        return img

    # Load the Data
    img = load_image()

    # Select the type of thresholding #
    thresholding_method = st.selectbox(label='Pilih metode thresholding yang diinginkan:',
                                       options=['Manual Thresholding',
                                                'Local Thresholding',
                                                'Global Thresholding'])
    
    if thresholding_method == 'Global Thresholding':
        global_thresholding.apply_threshold(img)
    
    elif thresholding_method == 'Local Thresholding':
        local_thresholding.apply_threshold(img)
    
    elif thresholding_method == 'Manual Thresholding':
        manual_thresholding.apply_threshold(img)
    
    
