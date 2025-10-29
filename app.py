import cv2
import streamlit as st
import numpy as np
from PIL import Image

st.title("Image zoom controller")
st.write("Upload an image and control zoom using buttons below")

# Upload image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

# Zoom control buttons
if "scale" not in st.session_state:
    st.session_state["scale"] = 1.0

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.image(img_array, caption="Original Image", use_container_width=True)

    st.markdown("---")
    st.subheader("Zoom Controls")

    zoom_in = st.button("Zoom In")
    zoom_out = st.button("Zoom Out")
    reset = st.button("Reset Zoom")

    if zoom_in:
        st.session_state["scale"] += 0.2
    elif zoom_out:
        st.session_state["scale"] = max(0.5, st.session_state["scale"] - 0.2)
    elif reset:
        st.session_state["scale"] = 1.0

    scale = st.session_state["scale"]
    st.write(f"**Current Zoom:** {scale:.2f}x")

    # Apply zoom
    h, w = img_array.shape[:2]
    new_w = int(w / scale)
    new_h = int(h / scale)
    x1 = (w - new_w) // 2
    y1 = (h - new_h) // 2

    cropped = img_array[y1:y1 + new_h, x1:x1 + new_w]
    resized = cv2.resize(cropped, (w, h))
    st.image(resized, channels="RGB", caption="Zoomed Image", use_container_width=True)

else:
    st.info("Please upload an image to start.")
