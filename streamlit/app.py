import streamlit as st

def main():
    # Set page configuration
    st.set_page_config(page_title='Dino Map', page_icon='🦖')

    # Create page header and description
    st.header('Dino Map :t-rex:')
    st.markdown('Insert brief description')

    # File uploader for images
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, use_column_width=True)

        # get classification from model
        # label image with classification
        # display interactive map
        # potentially display educational information along with map
        # allow user to upload another photo and restart process
    
if __name__ == "__main__":
    main()