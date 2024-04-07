import streamlit as st
import tensorflow as tf
import numpy as np
import keras


# load model, set cache to prevent reloading
@st.cache_resource(show_spinner=True)
def load_model():
    model = keras.models.load_model("./models/dinosaur_classifier.keras")
    return model


def load_image(image):
    img = tf.image.decode_jpeg(image, channels=3)
    img = tf.cast(img, tf.float32)
    img /= 255.0
    img = tf.image.resize(img, (224, 224))
    img = tf.expand_dims(img, axis=0)
    return img


def main():
    # Set page configuration
    st.set_page_config(page_title="Dino Map", page_icon="🦖")

    # Create page header and description
    st.header("Dino Map :t-rex:")
    st.markdown("Insert brief description")

    with st.spinner("Loading Model...."):
        model = load_model()

    classes = [
        "Ankylosaurus",
        "Brachiosaurus",
        "Compsognathus",
        "Corythosaurus",
        "Dilophosaurus",
        "Dimorphodon",
        "Gallimimus",
        "Pachycephalosaurus",
        "Parasaurolophus",
        "Spinosaurus",
        "Stegosaurus",
        "Triceratops",
        "Tyrannosaurus_Rex",
        "Velociraptor",
    ]

    # File uploader for images
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, use_column_width=True)

        st.write("Predicting Class...")

        with st.spinner("Classifying..."):
            img_tensor = load_image(uploaded_file.read())
            pred = model.predict(img_tensor)
            pred_class = classes[np.argmax(pred)]
            st.write("Predicted Class:", pred_class)

        # get classification from model
        # label image with classification
        # display interactive map
        # potentially display educational information along with map
        # allow user to upload another photo and restart process


if __name__ == "__main__":
    main()
