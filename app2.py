import streamlit as st

# Sample perfume data
perfumes = {
    "Floral Fresh": [
        "Daisy by Marc Jacobs", 
        "Flowerbomb by Viktor&Rolf",
        "J'adore by Dior"  # Added Dior perfume
    ],
    "Woody Oriental": [
        "Black Orchid by Tom Ford", 
        "Santal 33 by Le Labo"
    ],
    "Citrus Aromatic": [
        "Light Blue by Dolce & Gabbana", 
        "Acqua di Gio by Giorgio Armani",
        "Coco Mademoiselle by Chanel"  # Added Chanel perfume
    ],
    "Spicy": [
        "Spicebomb by Viktor&Rolf", 
        "Cinnamon Spice by Jo Malone"
    ],
    "Oriental Floral": [  # Added a new category for Gucci
        "Guilty by Gucci"
    ]
}
st.title('Perfume Recommendation App')

# User input for scent preference
scent_preference = st.selectbox('What is your preferred scent note?', list(perfumes.keys()))

# Displaying the recommendations based on user input
if st.button('Recommend Perfume'):
    st.write(f"Based on your preference for {scent_preference} scents, you might like:")
    for perfume in perfumes[scent_preference]:
        st.write(f"- {perfume}")
