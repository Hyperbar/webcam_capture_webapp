
import streamlit as st
from PIL import Image

def img_converter(image):
    # Convert pillow image to greyscale
    gray_img = image.convert("L")

    # Render the grayscale image on the webpage
    return st.image(gray_img, caption="Grayscale Image")

if __name__ == "__main__":
    st.title("Grayscale Image Converter")

    # Capture image from webcam
    camera_image = st.camera_input("Take a photo")

    if camera_image is not None:
        # Open the captured image
        img = Image.open(camera_image)

        # Display the original image
        st.image(img, caption="Original Image")

        # Display the image dimensions
        width, height = img.size
        st.write(f"Image dimensions: {width} x {height} pixels")

        # Convert and display the image in grayscale
        img_converter(img)

        # You can add other processing or options here

    else:
        st.write("Waiting for image capture...")