from PIL import Image
import numpy as np
import pandas as pd
import streamlit as st
import gzip
from io import BytesIO

st.title("Converter photos into csv file")
uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Photo", use_column_width=True)
    st.write("Photo uploaded successfully!")
    
    arr = np.array(image)
    height, width, channels = arr.shape
    flattened_array = arr.reshape(-1, channels)
    df = pd.DataFrame(flattened_array,columns=["Red", "Green", "Blue"])

    csv_buffer = BytesIO()
    with gzip.GzipFile(fileobj=csv_buffer, mode="w") as f:
        df.to_csv(f, index=False)

    csv_buffer.seek(0) 

    st.download_button(
        label="Download Compressed CSV",
        data=csv_buffer,
        file_name="large_image_data.csv.gz",
        mime="application/gzip"
    )
else:
    st.write("Please upload a photo.")

