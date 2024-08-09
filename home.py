import streamlit as st

def show_home_page():
    st.title("Welcome to the Salary Prediction Application!")
    st.image("C:\Streamlit-assignment1\salaryprediction.jpg", caption="Software Developer salary", use_column_width=True)
    st.write("""
    ### Discover Your Potential Earnings
    This application provides insights into the potential salaries for software developers based on various factors such as country, education level, and years of experience.

    ### Features
    - **Predict Your Salary**: Use our prediction model to estimate your salary.
    - **Data Visualization**: Explore visual representations of salary data from various countries and education levels.
    - **About Us**: Learn more about the technology and team behind this application.
    - **Contact Us**: Get in touch with us for any queries or feedback.

    ### How to Navigate
    Use the sidebar to navigate between different pages:
    - **Home**: This page.
    - **Predict Your Salary**: Predict your potential salary based on your profile.
    - **Visualizations**: View visual insights from the data.
    - **About**: Learn more about the application.
    - **Contact**: Reach out to us.

    """)
    


