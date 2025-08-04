import streamlit as st

# Set page configuration
st.set_page_config(page_title="Faizan Ali | Metallurgical Engineer", page_icon="🔩", layout="centered")

# Inject CSS for a modern, professional look
def set_custom_style():
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #e6f0ff, #f7faff);
                font-family: 'Segoe UI', sans-serif;
                padding: 2rem;
                color: #1f2937;
            }
            h1, h2, h3 {
                color: #003366;
            }
            .stMarkdown p {
                font-size: 17px;
                line-height: 1.6;
            }
            .css-zt5igj {
                font-size: 18px;
                font-weight: 500;
            }
            hr {
                border-top: 1px solid #cbd5e1;
            }
        </style>
    """, unsafe_allow_html=True)

# Apply style
set_custom_style()

# Title & contact
st.title("Faizan Ali")
st.subheader("Metallurgical Engineer | Materials Specialist | NDT Certified")
st.markdown("📍 Freiberg, Germany | 📧 faizanalidram@gmail.com | 📞 +49 15256046716")
st.markdown("---")

# About Me
st.header("👋 About Me")
st.write("""
I’m **Faizan Ali**, a passionate **Metallurgical Engineer** with hands-on experience in **non-destructive testing**, **steelmaking processes**, and **thermophysical property analysis**.

Born in **Hunza, Pakistan** and now based in **Freiberg, Germany**, I aim to contribute to innovative solutions that drive efficiency and quality in material science and production processes.
""")

# Education
st.header("🎓 Education")
st.markdown("""
**M.Sc. Metallic Materials Technology**  
📍 Technical University Bergakademie Freiberg, Germany (2021–2025)  
*Thesis:* Measurement of Thermophysical Properties of EAF Slag

**B.E. Metallurgical Engineering**  
📍 NED University of Engineering & Technology, Karachi, Pakistan (2015–2019)  
*Thesis:* FeO Reduction in EAF Slag to Improve Steelmaking Efficiency
""")

# Work Experience
st.header("💼 Work Experience")
st.markdown("""
**Werkstudent – Ringoplast Leubsdorf GmbH** *(Jul 2024 – Sep 2024)*  
**Intern – Helmholtz Institute Freiberg** *(Feb 2024 – May 2024)*  
**Werkstudent – Hitachi GmbH** *(Aug 2022 – Nov 2022)*  
**Trainee Engineer – NDT Premier Tubular Inspection Services** *(Jan 2021 – Mar 2021)*
""")

# Technical Skills
st.header("🛠️ Technical Skills")
st.markdown("""
- **Material Testing & Inspection:** NDT, Metallography, Visual & Ultrasonic Testing  
- **Software & Tools:** SolidWorks, AutoCAD, FACTSAGE, HSC Chemistry, Origin, MS Office  
- **Steelmaking Processes:** EAF slag modeling, refining techniques, thermodynamic analysis  
- **Languages:** English (C1), German (B1), Urdu (Native)
""")

# Key Projects
st.header("📌 Projects & Research")
st.markdown("""
- **EAF Slag Viscosity Modeling:** Simulated high-temp slag behavior using FACTSAGE and Origin.  
- **FeO Content Reduction Techniques:** Improved slag quality and process efficiency in steelmaking.  
- **Ultrasonic Testing & Metallography:** Assessed material integrity of casing joints and high-pressure pumps.  
- **Metals Recovery Thermodynamics:** Evaluated recovery using simulation tools like HSC Chemistry.
""")

# Certifications
st.header("📜 Certifications")
st.markdown("""
- Community Emergency Response Team (CERT)  
- First Aid and Casualty Handling  
- Occupational Health & Safety Training  
- Firefighting Procedures
""")

# Contact Info
st.header("📫 Contact & Profiles")
st.markdown("""
- ✉️ Email: faizanalidram@gmail.com  
- 📱 WhatsApp: +49 15256046716  
- 🔗 [LinkedIn](https://www.linkedin.com/in/faizan-ali-27197919b/)
""")

st.markdown("---")
st.caption("Crafted with Streamlit by Faizan Ali | Last Updated: 2025")
