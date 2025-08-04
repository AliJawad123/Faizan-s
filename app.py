import streamlit as st
from PIL import Image

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
            .profile-pic {
                border: 3px solid #1a237e;
                border-radius: 12px;
                display: block;
                margin-left: auto;
                margin-right: auto;
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

# Header section
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown('<img src="assests/faizan.jpeg" class="profile-pic" width="180">', unsafe_allow_html=True)
with col2:
    st.title("Faizan Ali")
    st.subheader("Metallurgical Engineer | Materials Testing & Quality Control")

# Aligned contact row
st.markdown("""
<div class="contact-row">
    <div>📧 faizanalidram@gmail.com</div>
    <div>📞 +49 15256046716</div>
    <div>📍 Freiberg, Germany</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# About Me
st.header("About Me")
st.write("""
I am a **Metallurgical Engineer** with academic training and international experience in **materials inspection**, **non-destructive testing (NDT)**, and **steelmaking processes**.

Originating from **Hunza, Pakistan**, and currently based in **Freiberg, Germany**, I focus on applying scientific principles to improve material reliability and process efficiency in industrial settings.

My interests include **thermodynamic modeling**, **structural analysis**, and contributing to safety-driven, quality-oriented engineering environments.
""")

# Education
st.header("Education")
st.markdown("""
**M.Sc. Metallic Materials Technology**  
📍 Technical University Bergakademie Freiberg, Germany (2021 – 2025)  
*Thesis:* Thermophysical Properties of Electric Arc Furnace (EAF) Slag  

**B.E. Metallurgical Engineering**  
📍 NED University of Engineering & Technology, Karachi, Pakistan (2015 – 2019)  
*Thesis:* FeO Content Optimization in EAF Slag for Enhanced Steelmaking
""")

# Work Experience
st.header("Professional Experience")
st.markdown("""
**Werkstudent – Ringoplast Leubsdorf GmbH** *(Jul 2024 – Sep 2024)*  
**Intern – Helmholtz Institute Freiberg for Resource Technology** *(Feb 2024 – May 2024)*  
**Werkstudent – Hitachi GmbH, Roßen** *(Aug 2022 – Nov 2022)*  
**Trainee Engineer – NDT Premier Tubular Inspection Services** *(Jan 2021 – Mar 2021)*
""")

# Technical Skills
st.header("Technical Skills")
st.markdown("""
- **Inspection & Testing:** NDT, Visual/Ultrasonic Testing, Metallography  
- **Modeling Tools:** FACTSAGE, HSC Chemistry, OriginLab  
- **CAD & Simulation:** SolidWorks, AutoCAD, Solid Edge  
- **Software Proficiency:** MS Office Suite, Report Writing, Data Analysis  
- **Languages:** English (C1), German (B1), Urdu (Native)
""")

# Projects
st.header("Projects & Research")
st.markdown("""
- **Thermophysical Modeling of Slag:** Used FACTSAGE and Origin to simulate high-temperature slag properties.  
- **FeO Reduction Studies:** Applied chemical and operational strategies for refining slag composition.  
- **Material Integrity Inspections:** Conducted metallographic and ultrasonic evaluation of high-pressure components.  
- **Metals Recovery:** Simulated thermodynamic recovery paths using HSC Chemistry.
""")

# Certifications
st.header("Certifications")
st.markdown("""
- Community Emergency Response Team (CERT)  
- First Aid & Casualty Handling  
- Fire Safety Procedures  
- Occupational Health & Safety
""")

# Contact
st.header("Contact & Profiles")
st.markdown("""
- 📧 Email: faizanalidram@gmail.com  
- 📱 WhatsApp: +49 15256046716  
- 🔗 [LinkedIn](https://www.linkedin.com/in/faizan-ali-27197919b/)
""")

st.markdown("---")
st.caption("Developed by Faizan Ali | Streamlit Profile | Last updated: 2025")
