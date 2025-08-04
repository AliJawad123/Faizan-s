import streamlit as st

# Custom background with CSS
def set_bg():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(to right, #f0f4f8, #d9e2ec);
            color: #1f2d3d;
            font-family: 'Segoe UI', sans-serif;
        }}
        .css-1v0mbdj p {{
            font-size: 16px;
        }}
        .stTitle {{
            color: #003366;
        }}
        .stHeader, .stSubheader {{
            color: #004080;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
set_bg()

# Page setup
st.set_page_config(page_title="Faizan Ali | Metallurgical Engineer", page_icon="🔩", layout="centered")

# Name and Title
st.title("Faizan Ali")
st.subheader("Metallurgical Engineer | Materials Specialist | NDT Certified")
st.markdown("📍 Freiberg, Germany | 📧 faizanalidram@gmail.com | 📞 +49 15256046716")

st.markdown("---")

# About Me
st.header("👋 About Me")
st.write("""
I’m **Faizan Ali**, a passionate Metallurgical Engineer with hands-on experience in non-destructive testing, steelmaking processes, and thermophysical property analysis.  
Born in Hunza, Pakistan, and currently based in Freiberg, Germany, I aim to contribute to innovative material science solutions that drive efficiency and quality in modern engineering.

With a strong foundation in **metallurgical thermodynamics**, **steel applications**, and **quality control**, I’m always seeking opportunities to merge academic rigor with industrial application.
""")

# Education
st.header("🎓 Education")
st.markdown("""
**M.Sc. Metallic Materials Technology**  
📍 Technical University Bergakademie Freiberg, Germany (2021–2025)  
*Thesis:* Measurement of Thermophysical Properties of EAF Slag

**B.E. Metallurgical Engineering**  
📍 NED University of Engineering & Technology, Karachi (2015–2019)  
*Thesis:* Reduction of FeO Content in EAF Slag for Steel Quality Enhancement
""")

# Experience
st.header("💼 Work Experience")
st.markdown("""
**Werkstudent – Ringoplast Leubsdorf GmbH** *(Jul 2024 – Sep 2024)*  
**Intern – Helmholtz-Institute Freiberg** *(Feb 2024 – May 2024)*  
**Werkstudent – Hitachi GmbH** *(Aug 2022 – Nov 2022)*  
**Trainee Engineer – NDT Premier Tubular Inspection Services** *(Jan 2021 – Mar 2021)*
""")

# Technical Skills
st.header("🛠️ Technical Skills")
st.markdown("""
- **Material Inspection:** NDT, Metallography, Visual/Ultrasonic Testing  
- **Software Tools:** SolidWorks, AutoCAD, FACTSAGE, HSC Chemistry, Origin  
- **Steelmaking Expertise:** EAF slag analysis, refining techniques, corrosion protection  
- **Other Tools:** MS Office, SEM/XRF analysis, Data Interpretation  
- **Languages:** English (C1), German (B1), Urdu (Native)
""")

# Key Projects
st.header("🔍 Key Projects & Research")
st.markdown("""
- **EAF Slag Analysis:** Modeled viscosity and surface tension properties for energy-efficient steelmaking.  
- **FeO Reduction in Steelmaking:** Investigated process optimization using carbon control strategies.  
- **Metallography & Inspection:** Supported failure analysis and reported material integrity using NDT methods.  
- **Metals Recovery Modeling:** Used HSC Chemistry and FACTSAGE for thermodynamic simulations.
""")

# Certificates
st.header("📜 Certifications")
st.markdown("""
- Community Emergency Response Team (CERT)  
- Firefighting and First Aid Training  
- Occupational Health & Safety Instruction
""")

# Contact & Socials
st.header("📫 Contact")
st.markdown("""
- 📧 Email: faizanalidram@gmail.com  
- 📱 WhatsApp: +49 15256046716  
- [LinkedIn Profile](https://www.linkedin.com/in/faizan-ali-27197919b/)
""")

st.markdown("---")
st.caption("Crafted with 🔧 by Faizan Ali using Streamlit | Updated 2025")
