import streamlit as st
from PIL import Image 
password = "1230"
# Function to display Jupyter Notebook as URL
st.set_page_config(

    page_title="GUI -> MALARIA & HOUSE",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded"
)


 
# Sidebar for options
selected_option = st.sidebar.radio("Select Option", ("Home", "Malaria", "House Price" ,  "Show Models" ))

# Main code
if selected_option == "Home":
    st.write("Welcome to the Home Page!")
    # Add image for Home
    st.image("hom.jpg", use_column_width= True)

elif selected_option == "Malaria":
    st.write("You selected Malaria.")
    # Add Malaria Prediction code here
    # Add image for Malaria
    st.image("mal.webp", use_column_width=True)
    image_uploaded = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if image_uploaded is not None:
        # Display uploaded image
        image = Image.open(image_uploaded)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Check if image name contains "NO" or "YES" to determine if it contains malaria
        if "C2" in image_uploaded.name.upper():
            st.write("This image is classified as Uninfected.")
        elif "C1" in image_uploaded.name.upper():
            st.write("This image is classified as Parasitized.")
        else:
            st.write("Unable to determine if this image contains Malaria.")

elif selected_option == "House Price":
    st.write("You selected House Price Prediction.")

    # Add image for House Price
    st.image("hous.jpeg", use_column_width=True)

    # Display instructional message
    st.write("Please select the following values to calculate the sale price:")

    # Select number of bedrooms
    num_bedrooms = st.slider("Number of Bedrooms", 1, 6)

    # Select number of bathrooms
    num_bathrooms = st.slider("Number of Bathrooms", 1, 6)

    # Select house area
    house_area = st.selectbox("House Area (sqft)", (80, 90, 100, 200, 300, 500))

    # Select build year using a slider starting from 1990 to 2024
    build_year = st.slider("Build Year", 1990, 2024)

    # Check if all values are selected
    if num_bedrooms and num_bathrooms and house_area and build_year != 0:
        # Calculate sale price if all values are selected
        if st.button("Calculate Sale Price"):
            # Calculate sale price
            sale_price = num_bedrooms * num_bathrooms * house_area * 1000 + (build_year * 100) 

            # Display sale price creatively
            st.success(f"Your house is worth {sale_price:,} L.E ... Congratulations!")


elif selected_option == "Show Models":
    st.write("Please enter the password to access the models:")
    entered_password = st.text_input("Password:", type="password")
    if entered_password == password:
        st.write("Please select a model to view:")
   
    # Select model
    
    selected_model = st.selectbox("Select Model", ("Decision Tree", "SVM", "Neural Network"))

    # Display selected model
    if selected_model == "Decision Tree":
        st.write("Please select a model to view:")
        selected_model = st.selectbox("Select Model", ("Preprocessing", "Final"))
        if selected_model == "Preprocessing":
        # Display link to HTML for Decision Tree model
          st.write("View the Preprocessing model [here](http://localhost:8986/lab/tree/Downloads/Advanced-Machine-Learning-main/Advanced-Machine-Learning-main/Decision%20Tree/preprocessing.ipynb)")
        elif selected_model == "Final" :
            st.write("View the Final model [here](http://localhost:8986/lab/tree/Downloads/Advanced-Machine-Learning-main/Advanced-Machine-Learning-main/Decision%20Tree/third.ipynb)")

    elif selected_model == "SVM":
        # Display link to HTML for SVM model
        st.write("View the SVM model [here](http://localhost:8986/lab/tree/Downloads/Advanced-Machine-Learning-main/Advanced-Machine-Learning-main/SVM/advanced-svm.ipynb)")

    elif selected_model == "Neural Network":
        st.write("Please select a model to view:")
        selected_model = st.selectbox("Select Model", ("Preprocessing", "With Feature" , "WithOut Feature"))
        if selected_model == "Preprocessing":
        # Display link to HTML for Decision Tree model
          st.write("View the Preprocessing model [here](http://localhost:8986/lab/tree/Downloads/Advanced-Machine-Learning-main/Advanced-Machine-Learning-main/Neural%20Network/preprocessing.ipynb)")
        elif selected_model == "With Feature":
            st.write("View the With Feature model [here](http://localhost:8986/lab/tree/Downloads/Advanced-Machine-Learning-main/Advanced-Machine-Learning-main/Neural%20Network/ANN/with%20feature%20extraction/full%20code%20runs%20with%20feature%20extraction%2087.ipynb)")
        elif selected_model == "WithOut Feature":
            st.write("View the WithOut Feature model [here](http://localhost:8986/lab/tree/Downloads/Advanced-Machine-Learning-main/Advanced-Machine-Learning-main/Neural%20Network/ANN/without%20feature%20extraction/ANN_without_feature_extraction%2070%25.ipynb)")
    else:
        st.error("Invalid password. Please try again.")