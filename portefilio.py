# app.py - Portfolio Streamlit Premium Gradient Violet/Blue
from pathlib import Path
import base64
import streamlit as st

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Portfolio — Anne Marietou Mendy",
    page_icon="💠",
    layout="wide"
)

# ---------- PREMIUM CSS ----------
st.markdown("""
<style>

* {font-family: 'Inter', sans-serif;}

body {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #3B82F6 100%) fixed !important;
}

/* HERO TITLE */
.hero-title {
    font-size: 3.2rem;
    font-weight: 900;
    text-align: left;
    background: linear-gradient(90deg, #E0E7FF, #C7D2FE, #A5B4FC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 6s infinite alternate;
}

@keyframes glow {
  from { opacity: 0.8; }
  to   { opacity: 1; }
}

/* CARDS - GLASSMORPHISM */
.section-card {
    padding: 28px;
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    transition: 0.35s ease;
}

.section-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.15);
}

/* SKILL BADGES */
.skill-badge {
    display: inline-block;
    padding: 6px 14px;
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    color: white;
    font-weight: 600;
    border-radius: 12px;
    margin: 4px;
    font-size: 0.85rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
}

/* BEAUTIFUL BUTTON */
.stButton>button {
    background: linear-gradient(90deg, #7C3AED, #4F46E5);
    color: white;
    font-weight: 700;
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #6D28D9, #4338CA);
}

/* SIDEBAR */
.sidebar-section {
    background-color: rgba(255,255,255,0.14);
    padding: 12px;
    border-radius: 12px;
    backdrop-filter: blur(10px);
}

/* FOOTER */
.footer {
    text-align:center;
    color: #E0E7FF;
    margin-top: 40px;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)

# ---------- CV ----------
PDF_PATH = Path("/mnt/data/Anne Marietou mendy (5).pdf")

def load_pdf_bytes(pdf_path: Path):
    return pdf_path.read_bytes() if pdf_path.exists() else None

def render_pdf_inline(pdf_bytes: bytes, height: int = 700):
    b64 = base64.b64encode(pdf_bytes).decode("utf-8")
    st.markdown(
        f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="{height}"></iframe>',
        unsafe_allow_html=True
    )

# ---------- DATA ----------
fullname = "Anne Marietou Mendy"
title = "Étudiante en Transformation Digitale — Développement & Chatbot — Odoo"
location = "Guédiawaye, Médina Gounass, Sénégal"
contact_email = "annemarietou.mendy@itd-hub.com"
phone = "+221 77 127 56 07"

short_bio = (
    "Étudiante en transformation digitale, passionnée par le développement, "
    "l’IA, les chatbots, l’e-commerce et les innovations technologiques."
)

skills = [
    "IA / Chatbots",
    "Rédaction technique",
    "ERP — Odoo",
    "E-commerce / Réseaux sociaux",
    "Développement web",
    "Agile / Scrum",
]

languages = [("Français", "Bon"), ("Anglais", "Débutante")]

experience_gtt = {
    "role": "Stagiaire — Intégration de solution IT",
    "company": "Grant Thornton Technologies (GTT)",
    "period": "sept. 2025 - nov. 2025",
    "location": "Dakar-Plateau, Sénégal",
    "description": (
        "Développement d’un chatbot interne, rédaction d’appels d’offres "
        "et contribution à des solutions digitales innovantes via Odoo."
    )
}

# ---------- SIDEBAR ----------
st.sidebar.title("💠 Portfolio Premium")
st.sidebar.header(fullname)
st.sidebar.write(title)
st.sidebar.write("📍 " + location)

pdf_bytes = load_pdf_bytes(PDF_PATH)
if pdf_bytes:
    st.sidebar.download_button("📄 Télécharger CV", pdf_bytes, "CV_Anne_Mendy.pdf", "application/pdf")

st.sidebar.markdown("---")
choice = st.sidebar.radio("Navigation", ["Accueil", "À propos", "Expériences", "Projets", "CV", "Contact"])


# ---------- PAGES ----------
if choice == "Accueil":
    st.markdown(f"<h1 class='hero-title'>Bonjour, je suis {fullname}</h1>", unsafe_allow_html=True)
    st.write("### " + title)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.subheader("✨ À propos de moi")
        st.write(short_bio)

        st.subheader("🔧 Compétences")
        for s in skills:
            st.markdown(f"<span class='skill-badge'>{s}</span>", unsafe_allow_html=True)

        st.subheader("🌍 Langues")
        for lang, level in languages:
            st.write(f"- **{lang}** — {level}")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.subheader("📞 Contact")
        st.write(contact_email)
        st.write(phone)

        st.subheader("🎓 Certifications")
        st.write("- Force N Data Analysis — 2025")
        st.write("- Force N Commerce Digital — 2023")
        st.write("- Force N Marketing Digital — 2023")
        st.markdown("</div>", unsafe_allow_html=True)


elif choice == "À propos":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("📘 À propos")
    st.write(short_bio)
    st.write("Je souhaite évoluer dans un environnement innovant…")
    st.markdown("</div>", unsafe_allow_html=True)


elif choice == "Expériences":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("💼 Expériences professionnelles")
    st.subheader(f"{experience_gtt['role']} — {experience_gtt['company']}")
    st.caption(f"{experience_gtt['period']} • {experience_gtt['location']}")
    st.write(experience_gtt["description"])
    st.markdown("</div>", unsafe_allow_html=True)


elif choice == "Projets":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("🚀 Projets")
    st.write("- **Chatbot interne** — Développé pendant mon stage chez GTT.")
    st.markdown("</div>", unsafe_allow_html=True)


elif choice == "CV":
    st.header("📄 Mon CV")
    if pdf_bytes:
        render_pdf_inline(pdf_bytes)
        st.download_button("Télécharger CV", pdf_bytes, "CV_Anne_Mendy.pdf", "application/pdf")


elif choice == "Contact":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("📬 Contact")
    st.write("📧 " + contact_email)
    st.write("📞 " + phone)

    with st.form("contact"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        submit = st.form_submit_button("Envoyer")
        if submit:
            st.success("Message prêt ✔️")
    st.markdown("</div>", unsafe_allow_html=True)


st.markdown("<p class='footer'>💠 Portfolio premium — Anne Marietou Mendy</p>", unsafe_allow_html=True)
