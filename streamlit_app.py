import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CRC1607 Summer School Application", layout="centered")

st.title("CRC1607 Summer School")
st.subheader("Summer School 2026 – Application Form")

st.write("""
The CRC1607 Summer School provides interdisciplinary training in:
- Ophthalmology
- Eye Research
- Ocular Inflammation
- Lymphangiogenesis
- Bioinformatics
- Metabolism
         

Please complete the application form and upload your CV and Motivation Letter.
""")

st.header("Personal Information")

first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
nationality = st.text_input("Nationality")

st.header("Academic Background")

degree = st.selectbox(
    "Current Degree",
    ["Bachelor", "Master", "PhD", "MD", "Other"]
)

field = st.text_input("Field of Study")
university = st.text_input("University / Institution")
country_uni = st.text_input("Country of University")

year = st.selectbox(
    "Year of Study",
    ["1", "2", "3", "4", "Final Year", "Other"]
)

st.header("Research Experience")

experience = st.radio("Do you have research experience?", ["Yes", "No"])

research_desc = st.text_area("Briefly describe your research experience")


st.header("Motivation")

motivation = st.text_area("Why do you want to attend the CRC1607 Summer School?")

gain = st.text_area("What do you hope to gain from this program?")

st.header("Upload Documents")

cv = st.file_uploader("Upload CV (PDF)", type=["pdf"])
motivation_letter = st.file_uploader("Upload Motivation Letter (PDF)", type=["pdf"])

st.header("Additional Information")

travel_support = st.radio("Do you require travel support?", ["Yes", "No"])


submit = st.button("Submit Application")

if submit:

    if cv and motivation_letter:

        os.makedirs("applications/cv", exist_ok=True)
        os.makedirs("applications/motivation", exist_ok=True)

        cv_path = f"applications/cv/{email}_cv.pdf"
        mot_path = f"applications/motivation/{email}_motivation.pdf"

        with open(cv_path, "wb") as f:
            f.write(cv.getbuffer())

        with open(mot_path, "wb") as f:
            f.write(motivation_letter.getbuffer())

        data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "Phone": phone,
            "Nationality": nationality,
            "Degree": degree,
            "Field": field,
            "University": university,
            "Country University": country_uni,
            "Year": year,
            "Experience": experience,
            "Research Description": research_desc,
            "Areas": ", ".join(areas),
            "Motivation": motivation,
            "Gain": gain,
            "Travel Support": travel_support,
            "Diet": diet
        }

        df = pd.DataFrame([data])

        file = "applications/applications.csv"

        if os.path.exists(file):
            df.to_csv(file, mode="a", header=False, index=False)
        else:
            df.to_csv(file, index=False)

        st.success("Application submitted successfully!")

    else:
        st.error("Please upload both CV and Motivation Letter.")