import streamlit as st
from PIL import Image
import base64
import os

# Page setup
st.set_page_config(page_title="Faizan Ali | Metallurgical Engineer", page_icon="🔧", layout="centered")

# Apply custom CSS
def set_custom_style():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #f1f5f9, #e2ecf8);
                font-family: 'Segoe UI', sans-serif;
                padding: 2rem;
                color: #1f2937;
            }
            h1, h2, h3 {
                color: #1a237e;
            }
            .stMarkdown p {
                font-size: 17px;
                line-height: 1.6;
            }
            .profile-pic-container {
                border: 3px solid #1a237e;
                padding: 6px;
                border-radius: 12px;
                width: fit-content;
                margin: auto;
            }
            .contact-row {
                display: flex;
                justify-content: center;
                gap: 30px;
                flex-wrap: wrap;
                font-size: 16px;
                color: #374151;
                margin-top: -20px;
            }
        </style>
    """, unsafe_allow_html=True)

set_custom_style()

# Profile Image Section
col1, col2 = st.columns([1, 3])
with col1:
    try:
        image = Image.open("assests/faizan.jpeg")
        st.markdown('<div class="profile-pic-container">', unsafe_allow_html=True)
        st.image(image, width=180)
        st.markdown('</div>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Profile image not found. Please place it in `assets/faizan.jpg`.")

with col2:
    st.title("Faizan Ali")
    st.subheader("Metallurgical Engineer | Materials Testing & Quality Control")

# Aligned Contact Info
st.markdown("""
<div class="contact-row">
    <div>📧 faizanalidram@gmail.com</div>
    <div>📞 +49 15256046716</div>
    <div>📍 Freiberg, Germany</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Sections continue...
st.header("About Me")
st.write("""
I am a **Metallurgical Engineer** with academic training and international experience in **materials inspection**, **non-destructive testing (NDT)**, and **steelmaking processes**.

Originating from **Hunza, Pakistan**, and currently based in **Freiberg, Germany**, I focus on applying scientific principles to improve material reliability and process efficiency in industrial settings.

My interests include **thermodynamic modeling**, **structural analysis**, and contributing to safety-driven, quality-oriented engineering environments.
""")

# (Remaining content continues unchanged below: Education, Experience, Skills, Projects, etc.)
