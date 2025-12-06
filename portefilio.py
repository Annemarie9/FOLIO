from pathlib import Path
import base64
import streamlit as st

# ----------------------------------------------------
# CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Portfolio — Anne Marietou Mendy",
    page_icon="💠",
    layout="wide"
)

# ----------------------------------------------------
# CUSTOM PREMIUM CSS (navbar + gradient + animations)
# ----------------------------------------------------
st.markdown("""
<style>

/* GLOBAL BACKGROUND */
body {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #3B82F6 100%) fixed !important;
}

/* NAVBAR */
.navbar {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(255,255,255,0.14);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(255,255,255,0.3);
    padding: 12px 30px;
    display: flex;
    justify-content: center;
    gap: 30px;
}

/* NAV BUTTON */
.nav-btn {
    padding: 10px 20px;
    border-radius: 12px;
    font-weight: 600;
    color: white !important;
    cursor: pointer;
    transition: 0.3s;
    text-decoration: none;
    background: rgba(255,255,255,0.08);
}

.nav-btn:hover {
    background: linear-gradient(90deg, #7C3AED, #4F46E5);
    transform: translateY(-3px);
}

/* ACTIVE PAGE */
.active {
    background: linear-gradient(90deg, #7C3AED, #4F46E5);
    box-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

/* HERO TITLE */
.hero-title {
    font-size: 3.2rem;
    font-weight: 900;
    background: linear-gradient(90deg, #E0E7FF, #C7D2FE, #A5B4FC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* GLASS CARD */
.section-card {
    padding: 30px;
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(14px);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.18);
    margin-top: 20px;
}

.skill-badge {
    display: inline-block;
    padding: 6px 14px;
    background: #4F46E5;
    color: white;
    border-radius: 10px;
    margin: 4px;
    font-size: 0.85rem;
}

.footer {
    text-align:center;
    color: #E0E7FF;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# SESSION STATE NAVIGATION
# ----------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Accueil"

def navigate(page):
    st.session_state.page = page


# ----------------------------------------------------
# NAVBAR
# ----------------------------------------------------
pages = ["Accueil", "À propos", "Expériences", "Projets", "CV", "Contact"]

navbar_html = "<div class='navbar'>"
for p in pages:
    active = "active" if st.session_state.page == p else ""
    navbar_html += f"<a class='nav-btn {active}' href='javascript:window.location.reload(false);' onclick=\"fetch('/_stcore/set_session_state?page={p}')\">{p}</a>"
navbar_html += "</div>"

# Inject navbar
st.markdown(navbar_html, unsafe_allow_html=True)


# ----------------------------------------------------
# DATA
# ----------------------------------------------------
PDF_PATH = Path("/mnt/data/Anne Marietou mendy (5).pdf")

fullname = "Anne Marietou Mendy"
title = "Étudiante en Transformation Digitale — Développement & Chatbot — Odoo"
location = "Guédiawaye, Médina Gounass, Sénégal"
contact_email = "annemarietou.mendy@itd-hub.com"
phone = "+221 77 127 56 07"

short_bio = (
    "Étudiante en transformation digitale, passionnée par le développement, "
    "l’IA, les chatbots et les innovations technologiques."
)

skills = [
    "IA / Chatbots",
    "Rédaction technique",
    "ERP — Odoo",
    "Développement web",
    "E-commerce",
    "Scrum / Agile",
]

experience_text = """
Développement d’un chatbot interne pour assister les consultants IT,  
rédaction d’appels d’offres et contribution à l’intégration de solutions digitales Odoo.
"""


# ----------------------------------------------------
# UTILS
# ----------------------------------------------------
def load_pdf_bytes(pdf_path: Path):
    return pdf_path.read_bytes() if pdf_path.exists() else None

def render_pdf(pdf):
    b64 = base64.b64encode(pdf).decode("utf-8")
    st.markdown(
        f'<iframe src="data:application/pdf;base64,{b64}" width="100%" height="700px"></iframe>',
        unsafe_allow_html=True
    )


# ----------------------------------------------------
# PAGES CONTENT
# ----------------------------------------------------
page = st.session_state.page

# ---------------- ACCUEIL ----------------
if page == "Accueil":
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
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.subheader("📞 Contact")
        st.write(contact_email)
        st.write(phone)
        st.markdown("</div>", unsafe_allow_html=True)


# ---------------- A PROPOS ----------------
elif page == "À propos":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("📘 À propos")
    st.write(short_bio)
    st.write("Je souhaite évoluer dans un environnement innovant…")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- EXPÉRIENCES ----------------
elif page == "Expériences":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("💼 Expériences professionnelles")
    st.subheader("Stagiaire IT — Grant Thornton Technologies (GTT)")
    st.caption("sept. 2025 — nov. 2025 • Dakar-Plateau")
    st.write(experience_text)
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- PROJETS ----------------
elif page == "Projets":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("🚀 Projets")
    st.write("- **Chatbot interne** — Développé pendant mon stage chez GTT.")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------------- CV ----------------
elif page == "CV":
    pdf = load_pdf_bytes(PDF_PATH)
    st.header("📄 Mon CV")
    if pdf:
        render_pdf(pdf)
        st.download_button("Télécharger CV", pdf, "CV_Anne_Mendy.pdf")


# ---------------- CONTACT ----------------
elif page == "Contact":
    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.header("📬 Contact")
    st.write("📧 " + contact_email)
    st.write("📞 " + phone)

    with st.form("contact"):
        name = st.text_input("Nom")
        email = st.text_input("Email")
        msg = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.success("Message envoyé ✔️")
    st.markdown("</div>", unsafe_allow_html=True)


# FOOTER
st.markdown("<p class='footer'>💠 Portfolio premium — Anne Marietou Mendy</p>", unsafe_allow_html=True)
