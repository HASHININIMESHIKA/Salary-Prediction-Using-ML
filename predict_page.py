import streamlit as st
import pickle
import numpy as np
#import sklearn


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor_loaded = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.image("slider.jpeg", use_column_width=True)
    st.title("Softaware Developers Salary Pediction")
    st.write("""### Dear Sir/Madam, We need some information to proceed with the prediction of your salary as a software developer, Thank you..!""")

    countries = (
        "United States of America",
        "Germany",
        "India",
        "Italy",
        "Canada",
        "Netherlands",
        "Brazil",	
        "France",	
        "Switzerland",	
        "Spain",
        "Austria",	
        "Russian Federation",	
        "Finland",	
        "Poland",	
        "Sweden",	
        "Belgium",	
        "Greece",	
        "Turkey",	
        "Israel",	
        "Portugal",	
        "Norway",	
        "Australia",
        "Latvia",	
        "Denmark",	
        "Sri Lanka",
        "Ukraine",	
        "Lithuania",	
        "Ireland",	
    )

    education = (
        "Bachelor’s degree",
        " Less than a Bachelors ",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country",countries)
    education = st.selectbox("Education Level",education)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Predict the Salary")
    if ok:
        x = np.array([[country, education, experience ]])
        x[:, 0] = le_country.transform(x[:,0])
        x[:, 1] = le_education.transform(x[:,1])
        x = x.astype(float)

        #print(sklearn.__version__)
        salary = regressor_loaded.predict(x)
        st.subheader(f"The predicted salary is ${salary[0]:.2f}")


