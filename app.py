import streamlit as st
from predict_page import show_predict_page
from visualization_page import show_visualization_page
from home import show_home_page
from about import show_about_page
from contact import show_contact_page
from comparison_page import show_comparison_page

page = st.sidebar.selectbox("Choose a page ", ("Home","About","Prediction", "Models Comparision", "Data Visualization","Contact Us"))


if page == "Home":
    show_home_page()
elif page == "About":
    show_about_page()
elif page == "Prediction":
    show_predict_page()
elif page == "Models Comparision":
    show_comparison_page()
elif page == "Data Visualization":
    show_visualization_page()
else: 
    show_contact_page()