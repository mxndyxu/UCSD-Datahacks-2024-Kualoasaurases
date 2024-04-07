import streamlit as st
import pandas as pd
import pylab 
import folium
from streamlit_folium import st_folium 
import matplotlib


def return_color_generator(NUM_COLORS, cmap='terrain'):
    """
    Generates color map for each dinosaur.
    """
    cm = pylab.get_cmap(cmap)
    for i in range(NUM_COLORS):
        color = cm(1.*i/NUM_COLORS)  # color will now be an RGBA tuple

    # or if you really want a generator:
    cgen = (cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS))

    return cgen 

# SOURCE: BugBytes from YouTube
# caching data to avoid reloading data every time the page is refreshed with decorator
@st.cache_data
def read_data(data_loc='../data/filtered_dino_fossil_locations.csv'):
    data = list()

    # data frame of dinosaur fossil locations across the world
    dino_fossil_locations = pd.read_csv(data_loc)

    dino_class_names = list(dino_fossil_locations['class_name'].unique())

    # generate colors for each dinosaur class
    dino_class_to_color = dict()
    # returns color generator that we can iterate through 
    cgen = return_color_generator(len(dino_class_names))
    for i, rgba in enumerate(cgen):
        dino_class = dino_class_names[i]
        HEXValue = matplotlib.colors.to_hex(rgba)
        dino_class_to_color[dino_class] = HEXValue
    
    # add colors to the data frame
    dino_fossil_locations['color'] = dino_fossil_locations['class_name'].map(dino_class_to_color)

    return dino_fossil_locations

def main():
    # Set page configuration
    st.set_page_config(page_title='DinoDetector', page_icon='🦖', layout='wide')

    # Create page header and description
    st.header(':t-rex: DinoDetector: Unearth the Past', divider='green')
    st.markdown('Welcome to our project for the 2024 UCSD DataHacks competition created by Aritra Das, Asif Mahdin, Luke Taylor, and Mandy Xu! Our project classifies an image of a dinosaur using transfer learning from a pre-trained network and finetuned to our dinosaurs dataset. An interactive map is displayed with the highlighted locations of where the classified dinosaur\'s fossils were found in the world.')
    st.markdown('To start, upload an image of a dinosaur. Once classified, explore the interactive map!')

    # File uploader for images
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        st.image(uploaded_file, use_column_width=True)
    
    # Dataframe preview of fossil locations
    data = read_data()
    st.subheader('Dataframe Preview')
    st.dataframe(data.head())

    data_class_names = list(data['class_name'].unique())
    m = folium.Map(location=(40.841852219046864, 56.94639806488843), zoom_start=2) # map

    # Display map and filters
    st.subheader('Locations of Dinosaur Fossils')
    dinosaur_input = st.multiselect('Select a Dinosaur:', tuple(data_class_names), default=data_class_names[0])
    data = data[data['class_name'].isin(dinosaur_input)]
    st.write('Hover over to see general dinosaur names. Click to see the specific dinosaur name.')
    for i, row in data.iterrows():
        location = (row['lat'], row['lng'])
        folium.CircleMarker(location, popup=row['accepted_name'], tooltip=row['class_name'], radius=5, color=row['color'],
        fill_color=row['color']).add_to(m)

    st_folium(m, width=1500)
    
if __name__ == "__main__":
    main()