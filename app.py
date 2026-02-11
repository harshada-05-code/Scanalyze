import streamlit as st
import cv2
import numpy as np

st.title("🩺 Scanalyze - Medical Image Analysis")

uploaded_file = st.file_uploader("Upload X-ray or MRI", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.success("⚠️ Anomaly Detected (Demo Output)")
