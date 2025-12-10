import streamlit as st
from PIL import Image
import pytesseract
import numpy as np

# Configure the page
st.set_page_config(page_title="OCR Pipeline", page_icon="📄")

st.title("📄 OCR Extraction App")
st.write("Upload an image to extract text using Tesseract OCR.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 1. Show the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # 2. Extract Text Button
    if st.button('Extract Text'):
        with st.spinner('Processing...'):
            try:
                # Convert PIL image to numpy array (if needed) or pass directly
                text = pytesseract.image_to_string(image)
                
                # Show results
                st.success("Extraction Complete!")
                st.text_area("Extracted Text", text, height=300)
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Note: If running locally, make sure Tesseract is installed on your Mac.")
