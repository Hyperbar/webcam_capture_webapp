import streamlit as st
from PIL import Image
from gray_converter import img_converter

# Application title
st.title("Grayscale Image Converter")

# Option to upload an image
uploaded_image = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

# Option to capture an image with the webcam
with st.expander("Open Camera"):
    camera_image = st.camera_input("Take a photo")

# Variable to store the selected image
selected_image = None

# Check if an image has been uploaded or captured
if uploaded_image is not None:
    selected_image = uploaded_image
    source = "uploaded"
elif camera_image is not None:
    selected_image = camera_image
    source = "captured"

# Processing the selected image
if selected_image is not None:
    try:
        # Open the image with Pillow
        img = Image.open(selected_image)

        # Display the original image
        st.image(img, caption=f"{source.capitalize()} image")

        # Get and display the image size
        width, height = img.size
        st.write(f"Image size: {width} x {height} pixels")

        # Convert the image to grayscale
        img_converter(img)

    except Exception as e:
        st.error(f"An error occurred while processing the image: {str(e)}")

else:
    st.write("Waiting for an image... Please upload an image or take a photo.")