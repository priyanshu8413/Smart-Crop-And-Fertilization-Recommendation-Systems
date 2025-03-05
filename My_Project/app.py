import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(layout="wide")


# CSS for background image


# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "home"


# Function to switch pages
def navigate_to(page):
    st.session_state.page = page


# Home Page
if st.session_state.page == "home":
    page_bg_img = '''
                 <style>
                     .stApp {
                         background: url("https://i.pinimg.com/originals/a0/8f/de/a08fde1a5b62749ada7453ec27af12cd.jpg") no-repeat center center fixed;
                         background-size: cover;
                     }
                     .center-text {
                         text-align: center;
                         font-size: 80px !important;
                         font-weight: bold;
                         color: red;
                         padding: 100px;
                     }
                      div.stButton > button {
               font-size: 50px !important;
               font-weight: bold !important;
              padding: 15px 30px !important;
             background-color: green !important;
               color: white !important;
               border-radius: 10px !important;
              border: none !important;
               width: 60% !important;
    }
                     .title-text {
                         font-size: 80px !important;
                         font-weight: bold !important;
                         color: black;
                         text-align: center;
                         line-height: 1.1; 
                     }
                 </style>
                 '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown('<p class="title-text">Smart Crop And Fertilization Recommendation Systems For Precision Agriculture</p>', unsafe_allow_html=True)
    st.markdown('<p class="title-text">Choose an option below to proceed:</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(" Crop Recommendation"):
            navigate_to("crop")

    with col2:
        if st.button(" Fertilizer Recommendation"):
            navigate_to("fertilizer")

# Crop Recommendation Page
elif st.session_state.page == "crop":
    col1, col2 = st.columns(2)

    with col1:
        if st.button(" Home Page"):
            navigate_to("home")

    with col2:
        if st.button(" Fertilizer Recommendation"):
            navigate_to("fertilizer")
    with open("catboost_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

        # Load the label encoder
    with open("label_encoder.pkl", "rb") as le_file:
        label_encoder = pickle.load(le_file)
    page_bg_img = '''
                    <style>
                        .stApp {
                            background: url("https://i.imgur.com/VVRpyfa.jpeg") no-repeat center center fixed;
                            background-size: cover;
                        }
                        .center-text {
                            text-align: center;
                            font-size: 100px !important;
                            font-weight: bold;
                            color: black;
                            padding: 100px;
                        }
                        .title-text {
                            font-size: 80px !important;
                            font-weight: bold !important;
                            color:black;
                            text-align: center;
                            line-height: 1.1; 
                        }
                        /* Styling input fields like table */
                      div[data-baseweb="input"], div[data-baseweb="select"] {
                        border: 2px solid black !important;
                }
                input[type="text"] {
                 font-size: 50px !important; /* Adjust the size as needed */
                  font-weight: bold !important;
                  
                }
                div.stButton > button {
               font-size: 24px !important;
               font-weight: bold !important;
              padding: 15px 30px !important;
             background-color: green !important;
               color: white !important;
               border-radius: 10px !important;
              border: none !important;
               width: 50% !important;
    }
           div[data-testid="stForm"] button {
        font-size: 1000px !important;
        font-weight: bold !important;
        padding: 20px 10px !important;
        background-color:#fff3cd !important;
        color: red !important;
        border-radius: 5px !important;
        border: none !important;
        width: 60% !important;
        display: block;
        margin: auto;
    }
                
                    </style>
                    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # Enable full-width layout

    # Custom CSS to make form full-width

    st.markdown('<p class="title-text">Crop Recommendation App</p>', unsafe_allow_html=True)

    with st.form("Crop Form"):
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown('<p class="title-text">MacroNutrients</p>', unsafe_allow_html=True)
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black;  ">Nitrogen (kg/hec)</p>',
                unsafe_allow_html=True)
            nitrogen = st.text_input("Enter Value", key="nitrogen", placeholder="Enter Nitrogen Content",
                                     label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black;  ">Phosphorous (kg/hec)</p>',
                unsafe_allow_html=True)
            phosphorus = st.text_input("Enter Value", key="phosphorus", placeholder="Enter Phosphorous Content",
                                       label_visibility="collapsed")

            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; ">Potassium (kg/hec)</p>',
                unsafe_allow_html=True)
            potassium = st.text_input("Enter Value", key="potassium", placeholder="Enter Potassium Content",
                                      label_visibility="collapsed")

            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black ;">Organic Carbon (%)</p>',
                unsafe_allow_html=True)
            organic_carbon = st.text_input("Enter Value", key="organic_carbon", placeholder="Enter Organic Carbon %",
                                           label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; ">EC (ds/m)</p>',
                unsafe_allow_html=True)
            EC = st.text_input("Enter Value", key="EC", placeholder="Enter the EC Value ",
                               label_visibility="collapsed")
        with col2:
            st.markdown('<p class="title-text">MicroNutrients</p>', unsafe_allow_html=True)
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; margin-bottom:-5px">Cu (PPM)</p>',
                unsafe_allow_html=True)
            Cu = st.text_input("Enter Value", key="Cu", placeholder="Enter The Copper Content",
                               label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color:black; margin-bottom:-5px">B(PPM)</p>',
                unsafe_allow_html=True)
            B = st.text_input("Enter Value", key="B", placeholder="Enter Boron  Content",
                              label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; margin-bottom:-5px"> S(PPM)</p>',
                unsafe_allow_html=True)
            S = st.text_input("Enter Value", key="S", placeholder="Enter Sulphur Content",
                              label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; margin-bottom:-5px">Fe (PPM)</p>',
                unsafe_allow_html=True)
            Fe = st.text_input("Enter Value", key="Fe", placeholder="Enter iron Content",
                               label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; margin-bottom:-5px"> Zn(PPM)</p>',
                unsafe_allow_html=True)
            Zn = st.text_input("Enter Value", key="Zn", placeholder="Enter Zinc Content",
                               label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; margin-bottom:-5px">Mn (PPM)</p>',
                unsafe_allow_html=True)
            Mn = st.text_input("Enter Value", key="Mn", placeholder="Enter Mangenese Content",
                               label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 50px; font-weight: bold; color: black; margin-bottom:-5px">Ph</p>',
                unsafe_allow_html=True)
            Ph = st.text_input("Enter Value", key="Ph", placeholder="Enter Ph value",
                               label_visibility="collapsed")
        submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            # Convert inputs to float
            input_data = np.array([[float(nitrogen), float(phosphorus), float(potassium),
                                    float(organic_carbon), float(EC), float(Cu),
                                    float(B), float(S), float(Fe), float(Zn),
                                    float(Mn), float(Ph)]])

            # Debugging: Print input data
            print("Input Data for Prediction:", input_data)

            # Predict using model
            predicted_label = model.predict(input_data).flatten()[0]

            # Debugging: Print predicted label before encoding
            print("Predicted Label (Before Encoding):", predicted_label)

            # Convert numerical prediction back to original crop name
            recommended_crop = label_encoder.inverse_transform([int(predicted_label)])[0]

            # Debugging: Print final crop name
            print("Recommended Crop:", recommended_crop)

            # Display result in Streamlit
            st.markdown(
                f"""
                <div style="
                    padding: 60px;
                    background-color: #E8F5E9;
                    color: #1B5E20;
                    border-radius: 10px;
                    text-align: center;
                    font-size: 100px;
                    font-weight: bold;
                    border: 2px solid #1B5E20;
                ">
                    🌱 Recommended Crop: {recommended_crop} 🌱
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Prediction Error: {e}")



# Fertilizer Recommendation Page
elif st.session_state.page == "fertilizer":
    col1, col2 = st.columns(2)

    with col1:
        if st.button(" Home Page"):
            navigate_to("home")

    with col2:
        if st.button(" Crop Recommendation"):
            navigate_to("crop")
    page_bg_img = '''
             <style>
                .stApp {
                   background: url("https://i.imgur.com/qQZqrzU.jpeg") no-repeat center center fixed;
                   background-size: cover; 
                }
                 .title-text {
                   font-size: 150px !important;
                   font-weight: bold !important;
                   color: #fff3cd !important;
                   text-align: center;
                   line-height: 1.1; 
                }
                 div.stButton > button {
               font-size: 24px !important;
               font-weight: bold !important;
              padding: 15px 30px !important;
             background-color: green !important;
               color: white !important;
               border-radius: 10px !important;
              border: none !important;
               width: 50% !important;
    }
                label, .stTextInput label, .stSelectbox label {
                   font-weight: bold !important;
                   font-size: 200px !important;
                   color: yellow !important;
                  text-shadow:1px 1px 2px black;
                }

                /* Styling input fields like table */
               div[data-baseweb="input"], div[data-baseweb="select"] {
                  
                    border: 1px solid black !important;
                }
                input[type="text"] {
                 font-size: 50px !important; /* Adjust the size as needed */
                  font-weight: bold !important;
                  
                }
               
                div[data-testid="stForm"] button {
        font-size: 90px !important;
        font-weight: bold !important;
        padding: 20px 10px !important;
        background-color:#fff3cd  !important;
        color: red !important;
        border-radius: 5px !important;
        border: none !important;
        width: 60% !important;
        display: block;
        margin: auto;
    }
               /* Make output table headings bold and black */
                .bold-heading {
                   font-weight: bold;
                    color: black !important;
                }

                </style>
               '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown('<p class="title-text">Fertilizer Recommendation For Crops</p>', unsafe_allow_html=True)

    # Form for user input
    with st.form("Fertilizer_form"):


        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown(
                '<p style="font-size: 70px; font-weight: bold; color: yellow; margin-bottom:-5px">Nitrogen (kg/hec)</p>',
                unsafe_allow_html=True)
            nitrogen = st.text_input("Enter Value", key="nitrogen", placeholder="Enter Nitrogen Content",
                                     label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 70px; font-weight: bold; color: yellow; margin-bottom: -5px;">Phosphorous (kg/hec)</p>',
                unsafe_allow_html=True)
            phosphorus = st.text_input("Enter Value", key="phosphorus", placeholder="Enter Phosphorous Content",
                                       label_visibility="collapsed")

            st.markdown(
                '<p style="font-size: 70px; font-weight: bold; color: yellow; margin-bottom:-5px;">Potassium (kg/hec)</p>',
                unsafe_allow_html=True)
            potassium = st.text_input("Enter Value", key="potassium", placeholder="Enter Potassium Content",
                                      label_visibility="collapsed")
            st.markdown(
                '<p style="font-size: 70px; font-weight: bold; color: yellow; margin-bottom:-5px;">Target Amount Of Yield (kg/ha)</p>',
                unsafe_allow_html=True)
            target = st.text_input("Enter Value", key="target", placeholder="Enter Target Amount Of Yield",
                                      label_visibility="collapsed")



        submit = st.form_submit_button("Submit")

            # If submit button is clicked, show output
    if submit:
       
        st.markdown("<h3 class='bold-heading' >Recommended Fertilizers</h3>", unsafe_allow_html=True)

        # Creating the output table
        output_data = {
            "CROP": ["Sunflower (Class 4)"],
            "FERTILIZER NITROGEN ": ["131 kg per Hectare"],
            "FERTILIZER Phosporous": [
                " 181 Kg per Hectare"

            ],
            "FERTILIZER Potassium": [
                "48 Kg per Hectare  "

            ],
        }

        df = pd.DataFrame(output_data)

        table_html = f"""
                  <style>
                  

                      table {{

                          width: 3000px;
                          border-collapse: collapse;
                          text-align: center ;
                          font-size: 30px;
                          border-radius: 20px;
                          overflow: hidden;

                      }}
                      th, td {{
                          padding: 100px;
                          border: 1px solid black;
                          color: black;
                          font-size:40px !important;
                          font-weight:bold !important;
                         
                      }}
                      th {{
                          font-weight: bold;
                         justify-content: center;
                         align-items: center; 
                       
                         
                      }}
                       
                      th:nth-child(1), td:nth-child(1) {{ background-color: #ffcccb; }}  /* Light Red */
                      th:nth-child(2), td:nth-child(2) {{ background-color: #d4edda; }}  /* Light Green */
                      th:nth-child(3), td:nth-child(3) {{ background-color: #cce5ff; }}  /* Light Blue */
                      th:nth-child(4), td:nth-child(4) {{ background-color: #fff3cd; }}  /* Light Yellow */
                       
           
                  </style>
              <table>
              
              
       

                  """

        # Display the styled table
        st.markdown(table_html, unsafe_allow_html=True)
        # Display table with bold headers
        st.markdown(df.to_html(index=False, escape=False), unsafe_allow_html=True)

