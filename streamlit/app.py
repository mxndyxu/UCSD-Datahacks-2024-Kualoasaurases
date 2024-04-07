import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title='DinoDetector', page_icon='🦖')

    # Create page header and description
    st.header('DinoDetector: Unearth the Past :t-rex:', divider='green')
    st.markdown('Welcome to our project for the 2024 UCSD DataHacks competition created by Aritra Das, Asif Mahdin, Luke Taylor, and Mandy Xu! Our project classifies an image of a dinosaur using transfer learning from a pre-trained network and finetuned to our dinosaurs dataset. An interactive map is returned displaying the locations of where the classified dinosaur\'s fossils were found in the world.')
    st.markdown('To start, upload an image of a dinosaur. Once classified, explore the interactive map!')

    # File uploader for images
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, use_column_width=True)
    
if __name__ == "__main__":
    main()