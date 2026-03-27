import streamlit as st

st.set_page_config(
    page_title="EkoKalkulator – Prądziaki",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "ui_theme" not in st.session_state:
    st.session_state.ui_theme = "light"

CSS_LIGHT = r"""
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
}

/* === TŁO APLIKACJI === */
.stApp {
    background-color: #e8f5e9 !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #e8f5e9 !important;
}
[data-testid="stAppViewContainer"] > .main {
    background-color: #e8f5e9 !important;
}
[data-testid="block-container"] {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

/* Ukryj domyślny header/footer */
#MainMenu, header, footer { visibility: hidden; }

/* === ZAKŁADKI / RADIO === */
div[role="radiogroup"] {
    gap: 3px;
    background: #f1f8e9 !important;
    padding: 5px;
    border-radius: 14px;
    flex-wrap: wrap;
    border: 1px solid #c8e6c9;
    min-height: 2.65rem !important;
    align-items: center !important;
    box-sizing: border-box !important;
}
div[role="radiogroup"] label {
    background: transparent !important;
    border-radius: 10px !important;
    padding: 6px 8px !important;
    margin: 0 !important;
}
div[role="radiogroup"] label p {
    font-weight: 700 !important;
    font-size: 0.78rem !important;
    color: #1b5e20 !important;
}
div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
    display: none !important;
}
div[role="radiogroup"] label:has(input:checked) {
    background: #81c784 !important;
}
div[role="radiogroup"] label:has(input:checked) p {
    color: #0d2818 !important;
}

/* === PRZYCISKI === */
.stButton > button {
    background: #66bb6a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
    min-height: 3rem !important;
    width: 100% !important;
    letter-spacing: 0.01em !important;
    box-shadow: 0 2px 8px rgba(27, 94, 32, 0.2) !important;
    transition: background-color 0.15s ease, box-shadow 0.15s ease !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: #4caf50 !important;
    color: #ffffff !important;
}
.stButton > button:active {
    box-shadow: 0 1px 4px rgba(27, 94, 32, 0.35) !important;
}
.stButton > button:disabled {
    opacity: 0.55 !important;
    cursor: not-allowed !important;
}

/* === SUWAKI === */
.stSlider label, .stSlider p {
    color: #2e7d32 !important;
    font-weight: 600 !important;
    font-size: 0.93rem !important;
    line-height: 1.22 !important;
    white-space: nowrap !important;
}
.stSlider [data-testid="stWidgetLabel"] {
    white-space: nowrap !important;
    padding-top: 0.1rem !important;
    padding-bottom: 0.55rem !important;
    margin-bottom: 0.2rem !important;
}
.stSlider [data-testid="stMarkdownContainer"] p {
    white-space: nowrap !important;
}
div[data-testid="stVerticalBlock"]:has(.stSlider) [data-testid="stWidgetLabel"] {
    flex-wrap: nowrap !important;
}
/* Wartość liczbowa przy suwaku — bez „ramki” (pole/ tło) */
[data-testid="stSliderThumbValue"] {
    color: #1b5e20 !important;
    font-weight: 800 !important;
    font-size: 1.02rem !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
}
[data-testid="stSliderThumbValue"] * {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
.stSlider input {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
    outline: none !important;
}
.stSlider [data-baseweb="input"] {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
}
[data-testid="stSliderThumbValue"] span[data-testid="stMarkdownContainer"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* === OGÓLNE ETYKIETY === */
label, p {
    color: #2e7d32 !important;
}

/* === HEADINGI === */
h1, h2, h3, h4, h5 {
    color: #1b5e20 !important;
}

/* === KARTY === */
.welcome-card {
    background: linear-gradient(145deg, #c8e6c9, #e8f5e9);
    border: 1px solid #a5d6a7;
    color: #1b5e20;
    border-radius: 20px;
    padding: 28px 22px 24px;
    margin: 6px 0 14px;
    text-align: center;
    box-shadow: 0 6px 24px rgba(27, 94, 32, 0.12);
}
.welcome-card .emoji {
    font-size: 2.6rem;
    margin-bottom: 8px;
}
.welcome-card h2 {
    font-size: 1.4rem;
    font-weight: 900;
    margin-bottom: 10px;
    color: #1b5e20;
    line-height: 1.35;
}
.welcome-card p {
    font-size: 0.93rem;
    color: #2e7d32 !important;
    line-height: 1.65;
    margin: 0;
}
.welcome-card strong {
    color: #1b5e20 !important;
}

.info-card {
    background: #f1f8e9;
    border: 1px solid #c5e1a5;
    border-left: 4px solid #66bb6a;
    border-radius: 14px;
    padding: 16px 18px;
    margin: 10px 0 6px;
    color: #2e7d32 !important;
    font-size: 0.92rem;
    line-height: 1.6;
}
.info-card b {
    color: #1b5e20 !important;
}

.section-title {
    font-size: 1.1rem;
    font-weight: 900;
    color: #1b5e20 !important;
    margin: 16px 0 8px;
}

.tip-box {
    background: #f1f8e9;
    border: 1.5px dashed #c8e6c9;
    border-radius: 12px;
    padding: 13px 15px;
    margin: 8px 0 14px;
    font-size: 0.88rem;
    color: #1b5e20 !important;
    line-height: 1.55;
}

.result-card {
    background: #ffffff;
    border: 1px solid #c8e6c9;
    border-radius: 16px;
    padding: 16px 10px;
    margin: 6px 0;
    text-align: center;
}
.result-card .rlabel {
    font-size: 0.73rem;
    color: #558b2f;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}
.result-card .rvalue {
    font-size: 1.65rem;
    font-weight: 900;
    color: #1b5e20;
    line-height: 1.1;
}
.result-card .runit {
    font-size: 0.8rem;
    color: #43a047;
    font-weight: 700;
    margin-top: 2px;
}

.total-card {
    background: linear-gradient(135deg, #a5d6a7, #c8e6c9);
    border: 1px solid #81c784;
    border-radius: 20px;
    padding: 24px 20px;
    text-align: center;
    margin: 14px 0 18px;
    box-shadow: 0 6px 24px rgba(27, 94, 32, 0.15);
}
.total-card .tlabel {
    font-size: 0.78rem;
    color: #1b5e20;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.total-card .tvalue {
    font-size: 2.8rem;
    font-weight: 900;
    color: #0d2818;
    letter-spacing: -0.02em;
    line-height: 1.1;
}
.total-card .tsub {
    font-size: 0.82rem;
    color: #2e7d32;
    margin-top: 8px;
    opacity: 0.9;
}

.compare-card {
    background: #ffffff;
    border: 1px solid #c8e6c9;
    border-radius: 14px;
    padding: 13px 15px;
    margin: 6px 0;
    display: flex;
    align-items: center;
    gap: 13px;
}
.compare-card .cicon {
    font-size: 1.8rem;
    min-width: 36px;
    text-align: center;
}
.compare-card .cicon-coal {
    display: inline-block;
    filter: grayscale(1) brightness(0.12);
}
.compare-card .cval {
    font-size: 1.1rem;
    font-weight: 900;
    color: #1b5e20;
}
.compare-card .cdesc {
    font-size: 0.78rem;
    color: #558b2f;
    margin-top: 2px;
}

.footer-card {
    background: #f1f8e9;
    border: 1px solid #c8e6c9;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    margin-top: 12px;
}
.footer-card .fmsg {
    font-weight: 800;
    color: #1b5e20;
    font-size: 0.95rem;
    line-height: 1.55;
}
.footer-card .fsub {
    font-size: 0.76rem;
    color: #558b2f;
    margin-top: 8px;
}

.nav-top-spacer {
    height: 1.35rem;
    min-height: 1.35rem;
}

/* Przywitanie niżej — tylko odstęp, bez zmiany wyglądu kart */
.welcome-intro-spacer {
    height: 1.75rem;
    min-height: 1.75rem;
}

/* Motyw pionowo obok zakładek — góra motywu = góra paska zakładek */
div[data-testid="stHorizontalBlock"]:has(.theme-pill-wrap--inline) {
    align-items: flex-start !important;
}
div[data-testid="stHorizontalBlock"]:has(.theme-pill-wrap--inline) > div[data-testid="column"]:nth-child(2) {
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    align-items: flex-end !important;
    padding-left: 0.5rem !important;
}
.theme-pill-wrap--inline {
    width: auto;
    min-width: 2.5rem;
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;
}
.theme-pill-wrap--inline div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 3px !important;
    width: auto !important;
    max-width: none !important;
    min-width: 2.5rem !important;
    min-height: auto !important;
    margin: 0 !important;
    padding: 5px !important;
    border-radius: 14px !important;
    box-sizing: border-box !important;
    box-shadow: 0 2px 10px rgba(27, 94, 32, 0.14) !important;
}
.theme-pill-wrap--inline div[role="radiogroup"] label {
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: 0 !important;
    padding: 6px 8px !important;
    border-radius: 10px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.theme-pill-wrap--inline div[role="radiogroup"] label p {
    text-align: center !important;
    font-size: 0.92rem !important;
    line-height: 1 !important;
    margin: 0 !important;
}
/* Słońce — lekko cieplej; księżyc — szary, niepełny (🌒) */
.theme-pill-wrap--inline div[role="radiogroup"] label:nth-child(1) p {
    filter: saturate(1.25) brightness(1.02);
}
.theme-pill-wrap--inline div[role="radiogroup"] label:nth-child(2) p {
    filter: grayscale(1) brightness(0.72);
}
.theme-pill-wrap--inline div[role="radiogroup"] label:nth-child(2):has(input:checked) p {
    filter: grayscale(0.85) brightness(0.92);
}
"""

CSS_DARK = r"""
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
}

/* === TRYB CIEMNY — wyłącznie kolory (eco) === */
.stApp {
    background-color: #0f1f15 !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #0f1f15 !important;
}
[data-testid="stAppViewContainer"] > .main {
    background-color: #0f1f15 !important;
}
[data-testid="block-container"] {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

#MainMenu, header, footer { visibility: hidden; }

div[role="radiogroup"] {
    gap: 3px;
    background: #1a2e22 !important;
    padding: 5px;
    border-radius: 14px;
    flex-wrap: wrap;
    border: 1px solid #2d4a3a;
    min-height: 2.65rem !important;
    align-items: center !important;
    box-sizing: border-box !important;
}
div[role="radiogroup"] label {
    background: transparent !important;
    border-radius: 10px !important;
    padding: 6px 8px !important;
    margin: 0 !important;
}
div[role="radiogroup"] label p {
    font-weight: 700 !important;
    font-size: 0.78rem !important;
    color: #a5d6a7 !important;
}
div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
    display: none !important;
}
div[role="radiogroup"] label:has(input:checked) {
    background: #2e7d32 !important;
}
div[role="radiogroup"] label:has(input:checked) p {
    color: #f1f8e9 !important;
}

.stButton > button {
    background: #388e3c !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
    min-height: 3rem !important;
    width: 100% !important;
    letter-spacing: 0.01em !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.35) !important;
    transition: background-color 0.15s ease, box-shadow 0.15s ease !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: #43a047 !important;
    color: #ffffff !important;
}
.stButton > button:active {
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.45) !important;
}
.stButton > button:disabled {
    opacity: 0.55 !important;
    cursor: not-allowed !important;
}

.stSlider label, .stSlider p {
    color: #b2dfdb !important;
    font-weight: 600 !important;
    font-size: 0.93rem !important;
    line-height: 1.22 !important;
    white-space: nowrap !important;
}
.stSlider [data-testid="stWidgetLabel"] {
    white-space: nowrap !important;
    padding-top: 0.1rem !important;
    padding-bottom: 0.55rem !important;
    margin-bottom: 0.2rem !important;
}
.stSlider [data-testid="stMarkdownContainer"] p {
    white-space: nowrap !important;
}
div[data-testid="stVerticalBlock"]:has(.stSlider) [data-testid="stWidgetLabel"] {
    flex-wrap: nowrap !important;
}
[data-testid="stSliderThumbValue"] {
    color: #e8f5e9 !important;
    font-weight: 800 !important;
    font-size: 1.02rem !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
}
[data-testid="stSliderThumbValue"] * {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
.stSlider input {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
    outline: none !important;
}
.stSlider [data-baseweb="input"] {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
}
[data-testid="stSliderThumbValue"] span[data-testid="stMarkdownContainer"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

label, p {
    color: #b2dfdb !important;
}

h1, h2, h3, h4, h5 {
    color: #e8f5e9 !important;
}

.welcome-card {
    background: linear-gradient(145deg, #1b3d2a, #14261c);
    border: 1px solid #2d5a45;
    color: #e8f5e9;
    border-radius: 20px;
    padding: 28px 22px 24px;
    margin: 6px 0 14px;
    text-align: center;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.45);
}
.welcome-card .emoji {
    font-size: 2.6rem;
    margin-bottom: 8px;
}
.welcome-card h2 {
    font-size: 1.4rem;
    font-weight: 900;
    margin-bottom: 10px;
    color: #e8f5e9;
    line-height: 1.35;
}
.welcome-card p {
    font-size: 0.93rem;
    color: #c8e6c9 !important;
    line-height: 1.65;
    margin: 0;
}
.welcome-card strong {
    color: #a5d6a7 !important;
}

.info-card {
    background: #1a2e22;
    border: 1px solid #2d4a3a;
    border-left: 4px solid #43a047;
    border-radius: 14px;
    padding: 16px 18px;
    margin: 10px 0 6px;
    color: #c8e6c9 !important;
    font-size: 0.92rem;
    line-height: 1.6;
}
.info-card b {
    color: #e8f5e9 !important;
}

.section-title {
    font-size: 1.1rem;
    font-weight: 900;
    color: #e8f5e9 !important;
    margin: 16px 0 8px;
}

.tip-box {
    background: #1a2e22;
    border: 1.5px dashed #2d5a45;
    border-radius: 12px;
    padding: 13px 15px;
    margin: 8px 0 14px;
    font-size: 0.88rem;
    color: #c8e6c9 !important;
    line-height: 1.55;
}

.result-card {
    background: #14261c;
    border: 1px solid #2d4a3a;
    border-radius: 16px;
    padding: 16px 10px;
    margin: 6px 0;
    text-align: center;
}
.result-card .rlabel {
    font-size: 0.73rem;
    color: #81c784;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}
.result-card .rvalue {
    font-size: 1.65rem;
    font-weight: 900;
    color: #f1f8e9;
    line-height: 1.1;
}
.result-card .runit {
    font-size: 0.8rem;
    color: #a5d6a7;
    font-weight: 700;
    margin-top: 2px;
}

.total-card {
    background: linear-gradient(135deg, #1b3d2a, #1a4d35);
    border: 1px solid #2d5a45;
    border-radius: 20px;
    padding: 24px 20px;
    text-align: center;
    margin: 14px 0 18px;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.45);
}
.total-card .tlabel {
    font-size: 0.78rem;
    color: #c8e6c9;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.total-card .tvalue {
    font-size: 2.8rem;
    font-weight: 900;
    color: #f1f8e9;
    letter-spacing: -0.02em;
    line-height: 1.1;
}
.total-card .tsub {
    font-size: 0.82rem;
    color: #a5d6a7;
    margin-top: 8px;
    opacity: 0.95;
}

.compare-card {
    background: #1a2e22;
    border: 1px solid #2d4a3a;
    border-radius: 14px;
    padding: 13px 15px;
    margin: 6px 0;
    display: flex;
    align-items: center;
    gap: 13px;
}
.compare-card .cicon {
    font-size: 1.8rem;
    min-width: 36px;
    text-align: center;
}
.compare-card .cicon-coal {
    display: inline-block;
    filter: grayscale(1) brightness(0.45) contrast(1.1);
}
.compare-card .cval {
    font-size: 1.1rem;
    font-weight: 900;
    color: #f1f8e9;
}
.compare-card .cdesc {
    font-size: 0.78rem;
    color: #a5d6a7;
    margin-top: 2px;
}

.footer-card {
    background: #1a2e22;
    border: 1px solid #2d4a3a;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    margin-top: 12px;
}
.footer-card .fmsg {
    font-weight: 800;
    color: #e8f5e9;
    font-size: 0.95rem;
    line-height: 1.55;
}
.footer-card .fsub {
    font-size: 0.76rem;
    color: #a5d6a7;
    margin-top: 8px;
}

.nav-top-spacer {
    height: 1.35rem;
    min-height: 1.35rem;
}

.welcome-intro-spacer {
    height: 1.75rem;
    min-height: 1.75rem;
}

div[data-testid="stHorizontalBlock"]:has(.theme-pill-wrap--inline) {
    align-items: flex-start !important;
}
div[data-testid="stHorizontalBlock"]:has(.theme-pill-wrap--inline) > div[data-testid="column"]:nth-child(2) {
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    align-items: flex-end !important;
    padding-left: 0.5rem !important;
}
.theme-pill-wrap--inline {
    width: auto;
    min-width: 2.5rem;
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;
}
.theme-pill-wrap--inline div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    justify-content: flex-start !important;
    gap: 3px !important;
    width: auto !important;
    max-width: none !important;
    min-width: 2.5rem !important;
    min-height: auto !important;
    margin: 0 !important;
    padding: 5px !important;
    border-radius: 14px !important;
    box-sizing: border-box !important;
    background: #1a2e22 !important;
    border: 1px solid #2d4a3a !important;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.35) !important;
}
.theme-pill-wrap--inline div[role="radiogroup"] label {
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: 0 !important;
    padding: 6px 8px !important;
    border-radius: 10px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.theme-pill-wrap--inline div[role="radiogroup"] label p {
    text-align: center !important;
    font-size: 0.92rem !important;
    line-height: 1 !important;
    margin: 0 !important;
}
.theme-pill-wrap--inline div[role="radiogroup"] label:nth-child(1) p {
    filter: saturate(1.25) brightness(1.02);
}
.theme-pill-wrap--inline div[role="radiogroup"] label:nth-child(2) p {
    filter: grayscale(1) brightness(0.72);
}
.theme-pill-wrap--inline div[role="radiogroup"] label:nth-child(2):has(input:checked) p {
    filter: grayscale(0.85) brightness(0.92);
}
"""

st.markdown(
    "<style>\n"
    + (CSS_LIGHT if st.session_state.ui_theme == "light" else CSS_DARK)
    + "\n</style>",
    unsafe_allow_html=True,
)

defaults = {
    'sale_lekcyjne': 40,
    'przerwy_godz': 1.5,
    'cena_pradu': 1.05,
    'cena_ciepla': 110.0,
    'inne_pomieszczenia': 25,
    'proc_swiatla': 30,
    'urzadzenia': 135,
    'proc_standby': 40,
    'wietrzenia_dzien': 4,
    'proc_wietrzenie': 55,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

if "page" not in st.session_state:
    st.session_state.page = 0

tabs = ["🏠 Start", "💡 Oświetlenie", "🔌 Standby", "🔥 Ogrzewanie", "📊 Wyniki"]

NAV_RADIO_KEY = "nav_radio_tabs"
SYNC_NAV_FLAG = "_sync_nav_from_page"

# Nie wolno zmieniać wartości klucza widżetu po utworzeniu st.radio.
# Po „Dalej” / „Wróć” ustawiamy tylko page + flagę; tu — przed radio — sync do tabs[page].
if st.session_state.pop(SYNC_NAV_FLAG, False):
    st.session_state[NAV_RADIO_KEY] = tabs[st.session_state.page]
elif NAV_RADIO_KEY not in st.session_state:
    st.session_state[NAV_RADIO_KEY] = tabs[st.session_state.page]


def go_to_page(idx: int) -> None:
    st.session_state.page = idx
    st.session_state[SYNC_NAV_FLAG] = True
    st.rerun()


THEME_OPTIONS = ("☀️", "🌒")
_prev_theme = st.session_state.get("sel_theme")
if _prev_theme not in THEME_OPTIONS:
    if _prev_theme == "🌙":
        st.session_state.sel_theme = "🌒"
    else:
        st.session_state.sel_theme = "☀️" if st.session_state.ui_theme == "light" else "🌒"

# Która zakładka jest wybrana (stan widżetu z poprzedniego przebiegu) — przed wyrenderowaniem paska
_preview_tab = tabs.index(st.session_state[NAV_RADIO_KEY])
if _preview_tab == 0:
    st.markdown('<div class="welcome-intro-spacer"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="welcome-card">
        <div class="emoji">🌿</div>
        <h2>Cześć! Witaj w EkoKalkulatorze</h2>
        <p>
            Kalkulator stworzony na potrzeby konkursu
            <strong>„Zasil Szkołę Pomysłem”</strong><br>
            przez zespół <strong>Prądziaki</strong><br>
            z Uniwersyteckiego I Liceum Ogólnokształcącego<br>
            im. Juliusza Słowackiego w Chorzowie.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <b>📋 Skąd pochodzą dane?</b><br><br>
        Wszystkie wartości domyślne zebraliśmy bezpośrednio w naszej szkole.
        Przesuwając suwaki, możesz dostosować kalkulator do
        <b>dowolnej innej szkoły</b> i sprawdzić, ile energii
        marnuje się właśnie tam.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="nav-top-spacer"></div>', unsafe_allow_html=True)

col_nav, col_theme = st.columns([6, 1], gap="small")
with col_nav:
    selected = st.radio(
        "",
        tabs,
        horizontal=True,
        key=NAV_RADIO_KEY,
    )
with col_theme:
    st.markdown('<div class="theme-pill-wrap theme-pill-wrap--inline">', unsafe_allow_html=True)
    st.radio(
        "",
        list(THEME_OPTIONS),
        horizontal=False,
        key="sel_theme",
        label_visibility="collapsed",
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.session_state.page = tabs.index(selected)

_motyw = "dark" if st.session_state.sel_theme == "🌒" else "light"
if _motyw != st.session_state.ui_theme:
    st.session_state.ui_theme = _motyw
    st.rerun()

if st.session_state.page == 0:
    st.markdown('<div class="section-title">⚙️ Dane podstawowe szkoły</div>', unsafe_allow_html=True)

    st.session_state.sale_lekcyjne = st.slider(
        "🏫 Ilość sal lekcyjnych",
        min_value=5, max_value=80,
        value=int(st.session_state.sale_lekcyjne), step=1
    )
    st.session_state.przerwy_godz = st.slider(
        "⏱️ Przerwy łącznie (godz.)",
        min_value=0.5, max_value=4.0,
        value=float(st.session_state.przerwy_godz), step=0.05,
        format="%.2f h"
    )
    st.session_state.cena_pradu = st.slider(
        "⚡ Cena prądu (zł/kWh)",
        min_value=0.50, max_value=2.50,
        value=float(st.session_state.cena_pradu), step=0.01,
        format="%.2f zł"
    )
    st.session_state.cena_ciepla = st.slider(
        "🔥 Ciepło (zł/GJ)",
        min_value=20.0, max_value=350.0,
        value=float(st.session_state.cena_ciepla), step=1.0,
        format="%.0f zł"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    _, col_c, _ = st.columns([1, 4, 1])
    with col_c:
        if st.button("Dalej", key="btn_1", use_container_width=True):
            go_to_page(1)

elif st.session_state.page == 1:
    st.markdown('<div class="section-title">💡 Oświetlenie</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tip-box">
        Ile światła pali się niepotrzebnie podczas przerw?
        Uwzględniamy sale lekcyjne oraz inne pomieszczenia – toalety, szatnie, korytarze.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.inne_pomieszczenia = st.slider(
        "🚻 Inne pomieszczenia (toalety, korytarze…)",
        min_value=1, max_value=80,
        value=int(st.session_state.inne_pomieszczenia), step=1
    )
    st.session_state.proc_swiatla = st.slider(
        "🔦 % osób nie gaszących światła",
        min_value=0, max_value=100,
        value=int(st.session_state.proc_swiatla), step=1,
        format="%d%%"
    )

    s_kwh = (
        (st.session_state.sale_lekcyjne + st.session_state.inne_pomieszczenia)
        * st.session_state.przerwy_godz * 0.5
        * (st.session_state.proc_swiatla / 100) * 180
    )
    s_zl = s_kwh * st.session_state.cena_pradu

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">Marnowana energia</div>
            <div class="rvalue">{s_kwh:.0f}</div>
            <div class="runit">kWh / rok</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">Koszt strat</div>
            <div class="rvalue">{s_zl:.0f}</div>
            <div class="runit">zł / rok</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1, 2, 1])
    with b1:
        if st.button("Wróć", key="btn_back_1", use_container_width=True):
            go_to_page(0)
    with b3:
        if st.button("Dalej", key="btn_2", use_container_width=True):
            go_to_page(2)

elif st.session_state.page == 2:
    st.markdown('<div class="section-title">🔌 Tryb czuwania – Standby</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tip-box">
        Komputery, tablice multimedialne i rzutniki pozostawione włączone
        podczas przerw pobierają prąd bez żadnej potrzeby.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.urzadzenia = st.slider(
        "🖥️ Ilość urządzeń (PC, tablice, rzutniki…)",
        min_value=5, max_value=400,
        value=int(st.session_state.urzadzenia), step=1
    )
    st.session_state.proc_standby = st.slider(
        "🔴 % włączonych urządzeń podczas przerwy",
        min_value=0, max_value=100,
        value=int(st.session_state.proc_standby), step=1,
        format="%d%%"
    )

    sb_kwh = (
        st.session_state.urzadzenia
        * st.session_state.przerwy_godz
        * (st.session_state.proc_standby / 100)
        * 0.2 * 180
    )
    sb_zl = sb_kwh * st.session_state.cena_pradu

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">Marnowana energia</div>
            <div class="rvalue">{sb_kwh:.0f}</div>
            <div class="runit">kWh / rok</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">Koszt strat</div>
            <div class="rvalue">{sb_zl:.0f}</div>
            <div class="runit">zł / rok</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1, 2, 1])
    with b1:
        if st.button("Wróć", key="btn_back_2", use_container_width=True):
            go_to_page(1)
    with b3:
        if st.button("Dalej", key="btn_3", use_container_width=True):
            go_to_page(3)

elif st.session_state.page == 3:
    st.markdown('<div class="section-title">🔥 Ogrzewanie</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tip-box">
        Nieprawidłowe wietrzenie – zbyt długo lub przy szeroko otwartych oknach –
        powoduje ogromne straty ciepła w zimnych miesiącach.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.wietrzenia_dzien = st.slider(
        "🌬️ Ilość wietrzeń dziennie",
        min_value=1, max_value=15,
        value=int(st.session_state.wietrzenia_dzien), step=1
    )
    st.session_state.proc_wietrzenie = st.slider(
        "❌ % osób nieprawidłowo wietrzących sale",
        min_value=0, max_value=100,
        value=int(st.session_state.proc_wietrzenie), step=1,
        format="%d%%"
    )

    c_gj = (
        st.session_state.sale_lekcyjne
        * (st.session_state.proc_wietrzenie / 100)
        * 0.005
        * st.session_state.wietrzenia_dzien * 180
    )
    c_zl = c_gj * st.session_state.cena_ciepla

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">Marnowane ciepło</div>
            <div class="rvalue">{c_gj:.1f}</div>
            <div class="runit">GJ / rok</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">Koszt strat ciepła</div>
            <div class="rvalue">{c_zl:.0f}</div>
            <div class="runit">zł / rok</div></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1, 2, 1])
    with b1:
        if st.button("Wróć", key="btn_back_3", use_container_width=True):
            go_to_page(2)
    with b3:
        if st.button("Dalej", key="btn_4", use_container_width=True):
            go_to_page(4)

elif st.session_state.page == 4:
    _s_kwh = (
        (st.session_state.sale_lekcyjne + st.session_state.inne_pomieszczenia)
        * st.session_state.przerwy_godz * 0.5
        * (st.session_state.proc_swiatla / 100) * 180
    )
    _s_zl = _s_kwh * st.session_state.cena_pradu

    _sb_kwh = (
        st.session_state.urzadzenia
        * st.session_state.przerwy_godz
        * (st.session_state.proc_standby / 100)
        * 0.2 * 180
    )
    _sb_zl = _sb_kwh * st.session_state.cena_pradu

    _c_gj = (
        st.session_state.sale_lekcyjne
        * (st.session_state.proc_wietrzenie / 100)
        * 0.005
        * st.session_state.wietrzenia_dzien * 180
    )
    _c_zl = _c_gj * st.session_state.cena_ciepla

    _total_kwh = _s_kwh + _sb_kwh
    _total_zl = _s_zl + _sb_zl + _c_zl

    st.markdown('<div class="section-title">📊 Podsumowanie roczne</div>', unsafe_allow_html=True)

    st.markdown("#### ⚡ Energia elektryczna")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">💡 Oświetlenie</div>
            <div class="rvalue">{_s_kwh:.0f}</div>
            <div class="runit">kWh / rok</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">💡 Koszt</div>
            <div class="rvalue">{_s_zl:.0f}</div>
            <div class="runit">zł / rok</div></div>""", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">🔌 Standby</div>
            <div class="rvalue">{_sb_kwh:.0f}</div>
            <div class="runit">kWh / rok</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">🔌 Koszt</div>
            <div class="rvalue">{_sb_zl:.0f}</div>
            <div class="runit">zł / rok</div></div>""", unsafe_allow_html=True)

    st.markdown("#### 🔥 Energia cieplna")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">🔥 Straty</div>
            <div class="rvalue">{_c_gj:.1f}</div>
            <div class="runit">GJ / rok</div></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="result-card">
            <div class="rlabel">🔥 Koszt</div>
            <div class="rvalue">{_c_zl:.0f}</div>
            <div class="runit">zł / rok</div></div>""", unsafe_allow_html=True)

    total_str = f"{_total_zl:,.0f}".replace(",", "\u202f")
    st.markdown(f"""
    <div class="total-card">
        <div class="tlabel">💰 Łączny koszt zmarnowanej energii rocznie</div>
        <div class="tvalue">{total_str} zł</div>
        <div class="tsub">{_total_kwh:.0f} kWh energii elektrycznej &nbsp;+&nbsp; {_c_gj:.1f} GJ ciepła</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🌍 To tyle samo co…</div>', unsafe_allow_html=True)

    co2_kg = _total_kwh * 0.75
    drzewa = max(1, int(co2_kg / 22))
    co2_tony = round(co2_kg / 1000, 2)
    ton_wegla = round(_total_kwh * 0.00034, 2)
    km_auto = int(_total_kwh * 6.5)
    # Papier toaletowy ze stokrotkami — orientacyjnie 16 rolek = 12 zł (ile rolek można kupić za zmarnowany koszt)
    pln_za_16_rolek = 12.0
    rolek_w_opakowaniu = 16
    cena_za_rolke = pln_za_16_rolek / rolek_w_opakowaniu
    rolki = int(_total_zl / cena_za_rolke) if cena_za_rolke > 0 else 0

    comparisons = [
        ("🌳", f"{drzewa} drzew", "tyle drzew musiałoby rosnąć rok, by pochłonąć tyle CO₂"),
        ("☁️", f"{co2_tony} t CO₂", "tyle dwutlenku węgla zostało wyemitowane"),
        ('<span class="cicon-coal">🪨</span>', f"{ton_wegla} t węgla", "tyle węgla spalono, by wyprodukować tę energię"),
        ("🚗", f"{km_auto:,} km".replace(",", "\u202f"), "tyle kilometrów przejechałby samochód"),
        (
            "🧻",
            f"{rolki:,} rolek".replace(",", "\u202f"),
            "tyle rolek papieru toaletowego ze stokrotkami można by kupić za ten zmarnowany koszt",
        ),
    ]

    for icon, val, desc in comparisons:
        st.markdown(f"""
        <div class="compare-card">
            <div class="cicon">{icon}</div>
            <div>
                <div class="cval">{val}</div>
                <div class="cdesc">{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-card">
        <div style="font-size:1.4rem; margin-bottom:8px;">💚</div>
        <div class="fmsg">
            Zmieniając codzienne nawyki, wasza szkoła może zaoszczędzić
            energię, pieniądze i pomóc planecie!
        </div>
        <div class="fsub">
            EkoKalkulator – Prądziaki<br>
            Uniwersyteckie I LO im. Juliusza Słowackiego w Chorzowie
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1, 2, 1])
    with b1:
        if st.button("Wróć", key="btn_back_4", use_container_width=True):
            go_to_page(3)


