import streamlit as st

def show_about_page():
    st.title("About This Application")
    st.image("C:\Streamlit-assignment1\software_development.jpeg", caption="Software Development", use_column_width=True)
    st.write("""
    ### Welcome to the Salary Prediction Application!
    This application helps software developers predict their potential salary based on their profile.
    """)

    st.write("""
    #### Purpose
    The purpose of this application is to provide software developers with an estimate of their potential earnings based on factors like country, education level, and years of experience.
    
    #### Technology
    This application uses machine learning models trained on the Stack Overflow Developer Survey 2023 dataset. It leverages the power of the following technologies:
    - **Python**: For backend logic and machine learning.
    - **Streamlit**: For creating interactive web applications.
    - **Pandas**: For data manipulation.
    - **Matplotlib**: For data visualization.
    - **Scikit-Learn**: For machine learning model implementation.
    
    #### How It Works
    1. **Data Collection**: We collected data from the Stack Overflow Developer Survey 2023.
    2. **Data Cleaning**: The data was cleaned and processed to ensure accuracy.
    3. **Model Training**: A Decision Tree Regressor model was trained to predict salaries.
    4. **Prediction**: Users input their details, and the model predicts their potential salary.
    
    #### Team
    Developed by a committed undergraduate student at Horizon Campus, Sri Lanka, 
             this application showcases the innovative spirit and technical expertise of its creator. 
             Currently in their final year of study, they have a strong ambition to pursue advanced education 
             in Artificial Intelligence and Machine Learning. Their passion for technology and problem-solving drives their work, 
             aiming to make impactful contributions to the field. 
             This application is a testament to their dedication and forward-thinking approach to leveraging AI and ML.
    """)


