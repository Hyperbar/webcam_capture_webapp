"""import streamlit as st
from PIL import Image

# My webcam as conflict with streamlit, therefor i am using imp_img
# Otherwise replace imp_img by camera_image
#imp_img = "vintage-aesthetic-7131604_640.jpg"

camera_image = st.camera_input("Camera")

img = Image.open(camera_image)"""

import streamlit as st
from PIL import Image



# Titre de l'application
st.title("Capture d'image depuis la webcam")

with st.expander("Open Camera"):
    # Utilisation de st.camera_input pour capturer l'image
    camera_image = st.camera_input("Prenez une photo")

# Vérification si une image a été capturée
if camera_image is not None:
    # Ouverture de l'image capturée
    # create a pillow image
    img = Image.open(camera_image)

    # Affichage de l'image
    st.image(img, caption="Image capturée")

    # Vous pouvez ajouter ici d'autres traitements sur l'image
    st.write("Image capturée avec succès!")

    # Obtention de la taille de l'image
    width, height = img.size

    # Affichage de la taille sans parenthèses
    st.write(f"Taille de l'image : {width} x {height} pixels")
else:
    st.write("En attente de la capture d'image...")

if camera_image:
    # Convert pillow image to greyscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img, caption="Image niveaux de gris")

