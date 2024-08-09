import streamlit as st

def show_contact_page():
    st.title("Contact Us")
    st.image("contact.jpeg", caption="Get in Touch", use_column_width=True)

    st.write("""
    ### We'd love to hear from you!
    If you have any questions, feedback, or suggestions, please feel free to reach out to us.
    """)

    st.write("""
    #### Contact Information
    - **Email**: [hashininimeshikamg@gmail.com](mailto:contact@salarypredictor.com)
    - **Phone**: +94 717679884
    - **Address**: Malabe, Colombo, Sri Lanka.

    #### Social Media
    - [LinkedIn](https://www.linkedin.com/in/hashini-nimeshika-338b632ab/)
    - [GitHub](https://github.com/HASHININIMESHIKA)

    #### Feedback Form
    Please fill out the form below to send us your feedback.
    """)

    with st.form("feedback_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for your feedback!")

