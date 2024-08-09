# Salary-Prediction-Using-ML
Demo of Salary Prediction Using Machine Learning Algorithms

# Streamlit Web Developer Salary Prediction

## Overview
This project is a web application developed using Streamlit, which predicts the annual salary of software developers based on various features like country, education level, and years of professional experience. The application leverages machine learning models to provide accurate salary predictions and includes a comparison page to evaluate the performance of different models.

## Features
- **Salary Prediction**: Predict the annual salary of software developers based on user input.
- **Data Visualization**: Visualize and understand the underlying data used for predictions.
- **Model Comparison**: Compare the performance of different machine learning models using metrics such as Mean Squared Error and R-Squared.

## Project Structure
- **app.py**: The main entry point of the application.
- **predict_page.py**: Contains the code for the salary prediction page.
- **visualization_page.py**: Includes data visualization elements.
- **comparison_page.py**: Houses the logic for comparing different machine learning models.
- **survey_results_public.csv**: The dataset used for training and predictions.
- **requirements.txt**: Contains the necessary Python packages to run the application.

## Installation

### Clone the Repository
```bash
git clone https://github.com/HASHININIMESHIKA/Streamlit_Web_Developer_Salary_Prediction.git
cd Streamlit_Web_Developer_Salary_Prediction

Install Dependencies
pip install -r requirements.txt

Run the Application
streamlit run app.py

Model Training and Evaluation
The application uses several machine learning models to predict software developer salaries:
Linear Regression
Decision Tree Regressor
Random Forest Regressor
Support Vector Regressor
K-Nearest Neighbors Regressor
The models were trained using a dataset that was cleaned and preprocessed to handle missing values and categorical variables. The application includes a comparison page that evaluates these models based on Mean Squared Error and R-Squared metrics.

Deployment
The application can be deployed on Streamlit Cloud. Ensure that the requirements.txt is up-to-date with all necessary dependencies.

Deployment Issues
If you encounter issues such as large file sizes exceeding GitHub's limits, consider using Git Large File Storage (LFS). For compatibility errors during deployment, make sure your input data is properly validated and matches the model's expected format.

About the Developer
This application was developed by Hashini Nimeshika, an undergraduate student at Horizon Campus, Sri Lanka, currently in the final year of their academic journey. With a keen interest in Artificial Intelligence and Machine Learning, this project reflects a passion for leveraging these technologies to solve real-world problems. The developer aims to pursue higher studies in AI and ML.


### Key Points Covered:
- **Overview** of the project and its purpose.
- **Features** available in the application.
- **Installation** and running instructions.
- **Model Training and Evaluation** details.
- **Deployment** information, including issues and solutions.
- **Progress Bar** addition in the comparison page.
- **About the Developer** section to give background information.
- **License** details for legal clarity.
- **Contact** information for further inquiries.
