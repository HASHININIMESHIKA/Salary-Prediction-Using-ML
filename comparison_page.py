import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv") 
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    def clean_experience(x):
        if x == 'More than 50 years':
            return 50
        if x == 'Less than 1 year':
            return 0.5
        return float(x)

    def clean_education(x):
        if 'Bachelor’s degree' in x:
            return 'Bachelor’s degree'
        if 'Master’s degree' in x:
            return 'Master’s degree'
        if 'Professional degree' in x or 'Other doctoral' in x:
            return 'Post grad'
        return 'Less than a Bachelors'

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    df['EdLevel'] = df['EdLevel'].apply(clean_education)

    return df

def train_model(X_train, y_train, X_test, y_test, model):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2, y_pred

def show_comparison_page():
    st.title("Model Comparison")
    st.image("comparision.jpg", caption="Comparision", use_column_width=True)
    st.write("""
    ### 
    Welcome to the Model Comparison page! Here, we present a comparative analysis of various machine learning models. This section is designed to help you understand how different models perform against each other based on key metrics and evaluation criteria. Explore the results to gain insights into their strengths and weaknesses, and make informed decisions for your project.
    """)

    df = load_data()

    # Features and target variable
    X = df[['YearsCodePro', 'EdLevel', 'Country']]
    y = df['Salary']

    # Encoding categorical variables
    X = pd.get_dummies(X, drop_first=True)

    # Splitting the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Standardizing the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(),
        "Random Forest": RandomForestRegressor(),
        
    }

    results = []

    # Initialize the progress bar
    progress_bar = st.progress(0)
    total_models = len(models)

    st.write("### Actual values vs predicted values")

    for i, (model_name, model) in enumerate(models.items()):
        mse, r2, y_pred = train_model(X_train, y_train, X_test, y_test, model)
        results.append({
            "Model": model_name,
            "Mean Squared Error": mse,
            "R-Squared": r2
        })

        # Update the progress bar
        progress_bar.progress((i + 1) / total_models)

        # Plot actual vs predicted
        fig, ax = plt.subplots()
        sns.scatterplot(x=y_test, y=y_pred, ax=ax)
        ax.set_xlabel("Actual Salary")
        ax.set_ylabel("Predicted Salary")
        ax.set_title(f"{model_name}: Actual vs Predicted Salary")
        st.pyplot(fig)

    results_df = pd.DataFrame(results)

    # Displaying the results
    st.write("### Model Performance Metrics")
    st.dataframe(results_df)

    # Plotting the comparison
    st.write("### Model Performance Comparison with R-Squared")

    fig, ax = plt.subplots()
    sns.barplot(x="Model", y="R-Squared", data=results_df, ax=ax)
    ax.set_title("R-Squared by Model")
    st.pyplot(fig)

    st.write("### Model Performance Comparison with Mean Squared Error")

    fig, ax = plt.subplots()
    sns.barplot(x="Model", y="Mean Squared Error", data=results_df, ax=ax)
    ax.set_title("Mean Squared Error by Model")
    st.pyplot(fig)

    # Completion message
    st.success("Model comparison completed!")


