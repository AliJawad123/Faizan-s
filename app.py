import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Faizan Ali | Metallurgical Engineer", page_icon="🔧", layout="centered")

# Apply custom styles
def set_custom_style():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #f1f5f9, #e2ecf8);
                font-family: 'Segoe UI', sans-serif;
                padding: 0;
                color: #1f2937;
            }
            h1, h2, h3 {
                color: #1a237e;
            }
            .title {
                text-align: center;
                font-size: 32px;
                font-weight: bold;
                margin-bottom: 0.2rem;
            }
            .subtitle {
                text-align: center;
                font-size: 20px;
                color: #374151;
                margin-bottom: 1rem;
            }
            .contact-row {
                text-align: center;
                font-size: 15px;
                color: #374151;
                margin-bottom: 2rem;
            }
            .contact-row a {
                color: #1a73e8;
                text-decoration: none;
            }
            .profile-wrapper {
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 0;
            }
            .profile-img {
                border: 3px solid #1a237e;
                border-radius: 12px;
                width: 220px;
            }
        </style>
    """, unsafe_allow_html=True)

# Load styles
set_custom_style()

# Centered profile image without margin
try:
    image = Image.open("assets/faizan.jpg")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, width=220, use_container_width=False)
        st.markdown('<style>img { border: 3px solid #1a237e; border-radius: 12px; }</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Profile image not found. Please place it in `assests/faizan.jpeg`.")

# Name and title
st.markdown('<div class="title">Faizan Ali</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Metallurgical Engineer | Materials Testing & Quality Control</div>', unsafe_allow_html=True)

# Contact Info
st.markdown("""
<div class="contact-row">
    📍 Freiberg, Germany | 
    📧 <a href="mailto:faizanalidram@gmail.com">faizanalidram@gmail.com</a> | 
    📞 +49 15256046716
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Add additional sections here...


st.markdown("---")
# About Me
st.header("About Me")
st.write("""
I am a **dedicated Metallurgical Engineer** with academic training and international work experience in **materials inspection, NDT techniques, and steelmaking processes**.  
Originating from **Hunza, Pakistan**, and currently pursuing a Master’s degree in **Metallic Materials Technology** in **Freiberg, Germany**, I focus on applying scientific principles to enhance material performance and process reliability in the metallurgical industry.

My professional interest lies at the intersection of **material integrity, thermodynamic modeling**, and **process optimization**, and I am motivated to contribute to technically rigorous, safety-conscious, and quality-driven teams.
""")

# Education
st.header("Education")
st.markdown("""
**M.Sc. Metallic Materials Technology**  
📍 Technical University Bergakademie Freiberg, Germany (2021 – 2025)  
*Thesis:* Measurement of Thermophysical Properties of EAF Slag  

**B.E. Metallurgical Engineering**  
📍 NED University of Engineering & Technology, Karachi, Pakistan (2015 – 2019)  
*Thesis:* Optimization of FeO Reduction in EAF Slag for Steel Quality Improvement
""")

# Work Experience
st.header("Professional Experience")
st.markdown("""
**Werkstudent – Ringoplast Leubsdorf GmbH** *(Jul 2024 – Sep 2024)*  
**Intern – Helmholtz Institute Freiberg for Resource Technology** *(Feb 2024 – May 2024)*  
**Werkstudent – Hitachi GmbH, Roßen, Germany** *(Aug 2022 – Nov 2022)*  
**Trainee Engineer – NDT Premier Tubular Inspection Services, Karachi** *(Jan 2021 – Mar 2021)*
""")

# Technical Skills
st.header("Technical Skills")
st.markdown("""
- **Material Testing & Inspection:** NDT, Visual/Ultrasonic Testing, Metallography  
- **Process Modeling Tools:** FACTSAGE, HSC Chemistry, OriginLab  
- **CAD & Design:** SolidWorks, AutoCAD, Solid Edge  
- **Software Proficiency:** MS Office Suite, Report Documentation, Data Analysis  
- **Metallurgical Knowledge:** Steelmaking, Thermodynamics, Corrosion Protection  
- **Languages:** English (C1), German (B1), Urdu (Native)
""")

# Projects
st.header("Projects & Research Work")
st.markdown("""
- **Thermophysical Modeling of EAF Slag:** Measured and modeled viscosity, surface tension, and density of slag at high temperatures using FACTSAGE and the Einstein-Roscoe equation.  
- **Optimization of FeO Reduction:** Investigated refining techniques and chemical control methods to minimize FeO in slag and improve steel purity.  
- **Casing Joint Inspections:** Performed ultrasonic and visual NDT inspections to ensure equipment reliability and safety.  
- **Metals Recovery Analysis:** Contributed to simulations of metal extraction using thermodynamic software tools.
""")

# Certifications
st.header("Certifications")
st.markdown("""
- Community Emergency Response Team (CERT)  
- First Aid and Casualty Handling  
- Fire Safety & Evacuation Procedures  
- Occupational Health and Safety Training
""")

# Contact
st.header("Contact & Links")
st.markdown("""
- 📧 Email: faizanalidram@gmail.com  
- 📱 WhatsApp: +49 15256046716  
- 🔗 [LinkedIn Profile](https://www.linkedin.com/in/faizan-ali-27197919b/)
""")

st.markdown("---")
st.caption("Developed by Faizan Ali | Streamlit Profile | Last updated: 2025")
