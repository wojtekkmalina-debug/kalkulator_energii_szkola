import streamlit as st
from datetime import date

st.set_page_config(
    page_title="EkoKalkulator – Prądziaki",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

today = date.today().strftime("%d.%m.%Y")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
}

/* === TŁO APLIKACJI === */
.stApp {
    background-color: #0f2318 !important;
}
[data-testid="stAppViewContainer"] {
    background-color: #0f2318 !important;
}
[data-testid="stAppViewContainer"] > .main {
    background-color: #0f2318 !important;
}
[data-testid="block-container"] {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

/* Ukryj domyślny header/footer */
#MainMenu, header, footer { visibility: hidden; }

/* === ZAKŁADKI === */
.stTabs [data-baseweb="tab-list"] {
    gap: 3px;
    background: #1a3528 !important;
    padding: 5px;
    border-radius: 14px;
    flex-wrap: wrap;
    border: 1px solid #2a5040;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px !important;
    padding: 6px 8px !important;
    font-weight: 700 !important;
    font-size: 0.78rem !important;
    color: #6ee7b7 !important;
    background: transparent !important;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    background: #22c55e !important;
    color: #0a1a10 !important;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* === PRZYCISKI === */
.stButton > button {
    background: #22c55e !important;
    color: #052e16 !important;
    border: none !important;
    border-radius: 14px !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 900 !important;
    font-size: 1.05rem !important;
    padding: 14px 0 !important;
    width: 100% !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 20px rgba(34,197,94,0.4) !important;
    transition: all 0.18s ease !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: #16a34a !important;
    color: #ffffff !important;
    box-shadow: 0 6px 26px rgba(34,197,94,0.55) !important;
    transform: translateY(-2px) !important;
}

/* === SUWAKI === */
.stSlider label, .stSlider p {
    color: #a3d9b8 !important;
    font-weight: 600 !important;
}
[data-testid="stSliderThumbValue"] {
    color: #22c55e !important;
    font-weight: 800 !important;
    background: #1a3528 !important;
}

/* === OGÓLNE ETYKIETY === */
label, p {
    color: #a3d9b8 !important;
}

/* === HEADINGI === */
h1, h2, h3, h4, h5 {
    color: #86efac !important;
}

/* === KARTY === */
.welcome-card {
    background: linear-gradient(145deg, #14532d, #166534);
    border: 1px solid rgba(34,197,94,0.3);
    color: #dcfce7;
    border-radius: 20px;
    padding: 28px 22px 24px;
    margin: 6px 0 14px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(0,0,0,0.45);
}
.welcome-card .emoji { font-size: 2.6rem; margin-bottom: 8px; }
.welcome-card h2 {
    font-size: 1.4rem;
    font-weight: 900;
    margin-bottom: 10px;
    color: #f0fdf4;
    line-height: 1.35;
}
.welcome-card p {
    font-size: 0.93rem;
    color: #bbf7d0 !important;
    line-height: 1.65;
    margin: 0;
}
.welcome-card strong { color: #86efac !important; }

.info-card {
    background: #1a3528;
    border: 1px solid #2a5040;
    border-left: 4px solid #22c55e;
    border-radius: 14px;
    padding: 16px 18px;
    margin: 10px 0 6px;
    color: #bbf7d0 !important;
    font-size: 0.92rem;
    line-height: 1.6;
}
.info-card b { color: #86efac !important; }

.section-title {
    font-size: 1.1rem;
    font-weight: 900;
    color: #86efac !important;
    margin: 16px 0 8px;
}

.tip-box {
    background: #1a3528;
    border: 1.5px dashed #2a5040;
    border-radius: 12px;
    padding: 13px 15px;
    margin: 8px 0 14px;
    font-size: 0.88rem;
    color: #86efac !important;
    line-height: 1.55;
}

.result-card {
    background: #1a3528;
    border: 1px solid #2a5040;
    border-radius: 16px;
    padding: 16px 10px;
    margin: 6px 0;
    text-align: center;
}
.result-card .rlabel {
    font-size: 0.73rem;
    color: #6ee7b7;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}
.result-card .rvalue {
    font-size: 1.65rem;
    font-weight: 900;
    color: #f0fdf4;
    line-height: 1.1;
}
.result-card .runit {
    font-size: 0.8rem;
    color: #4ade80;
    font-weight: 700;
    margin-top: 2px;
}

.total-card {
    background: linear-gradient(135deg, #14532d, #15803d);
    border: 1px solid rgba(34,197,94,0.4);
    border-radius: 20px;
    padding: 24px 20px;
    text-align: center;
    margin: 14px 0 18px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
.total-card .tlabel {
    font-size: 0.78rem;
    color: #86efac;
    font-weight: 700;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 6px;
}
.total-card .tvalue {
    font-size: 2.8rem;
    font-weight: 900;
    color: #f0fdf4;
    letter-spacing: -0.02em;
    line-height: 1.1;
}
.total-card .tsub {
    font-size: 0.82rem;
    color: #86efac;
    margin-top: 8px;
    opacity: 0.85;
}

.compare-card {
    background: #1a3528;
    border: 1px solid #2a5040;
    border-radius: 14px;
    padding: 13px 15px;
    margin: 6px 0;
    display: flex;
    align-items: center;
    gap: 13px;
}
.compare-card .cicon { font-size: 1.8rem; min-width: 36px; text-align: center; }
.compare-card .cval { font-size: 1.1rem; font-weight: 900; color: #f0fdf4; }
.compare-card .cdesc { font-size: 0.78rem; color: #6ee7b7; margin-top: 2px; }

.footer-card {
    background: #1a3528;
    border: 1px solid #2a5040;
    border-radius: 16px;
    padding: 18px;
    text-align: center;
    margin-top: 12px;
}
.footer-card .fmsg { font-weight: 800; color: #86efac; font-size: 0.95rem; line-height: 1.55; }
.footer-card .fsub { font-size: 0.76rem; color: #4ade80; margin-top: 8px; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE – domyślne wartości ze szkoły ────────────────
defaults = {
    'sale_lekcyjne':      40,
    'przerwy_godz':       1.5,
    'cena_pradu':         1.05,
    'cena_ciepla':        110.0,
    'inne_pomieszczenia': 25,
    'proc_swiatla':       30,
    'urzadzenia':         135,
    'proc_standby':       40,
    'wietrzenia_dzien':   4,
    'proc_wietrzenie':    55,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── ZAKŁADKI ───────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Start",
    "💡 Oświetlenie",
    "🔌 Standby",
    "🔥 Ogrzewanie",
    "📊 Wyniki",
])

# ═══════════════════════════════════════════════════════════════
# TAB 1 – START
# ═══════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="welcome-card">
        <div class="emoji">🌿</div>
        <h2>Cześć! Witaj w EkoKalkulatorze</h2>
        <p>
            Kalkulator stworzony na potrzeby konkursu
            <strong>„Zasil Szkołę Pomysłem"</strong><br>
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

    st.markdown('<div class="section-title">⚙️ Dane podstawowe szkoły</div>', unsafe_allow_html=True)

    st.session_state.sale_lekcyjne = st.slider(
        "🏫 Liczba sal lekcyjnych",
        min_value=5, max_value=80,
        value=int(st.session_state.sale_lekcyjne), step=1
    )
    st.session_state.przerwy_godz = st.slider(
        "⏱️ Łączny czas przerw w ciągu dnia (godz.)",
        min_value=0.5, max_value=4.0,
        value=float(st.session_state.przerwy_godz), step=0.05,
        format="%.2f h"
    )
    st.session_state.cena_pradu = st.slider(
        "⚡ Aktualna cena prądu (zł / kWh)",
        min_value=0.50, max_value=2.50,
        value=float(st.session_state.cena_pradu), step=0.01,
        format="%.2f zł"
    )
    st.session_state.cena_ciepla = st.slider(
        f"🔥 Cena energii cieplnej (zł / GJ)  —  cena na {today}",
        min_value=20.0, max_value=350.0,
        value=float(st.session_state.cena_ciepla), step=1.0,
        format="%.0f zł"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 4, 1])
    with col_c:
        st.button("Dalej  →  Oświetlenie 💡", key="btn_1")

# ═══════════════════════════════════════════════════════════════
# TAB 2 – OŚWIETLENIE
# ═══════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-title">💡 Oświetlenie</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tip-box">
        Ile światła pali się niepotrzebnie podczas przerw?
        Uwzględniamy sale lekcyjne oraz inne pomieszczenia – toalety, szatnie, korytarze.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.inne_pomieszczenia = st.slider(
        "🚻 Liczba innych pomieszczeń (toalety, szatnie, korytarze…)",
        min_value=1, max_value=80,
        value=int(st.session_state.inne_pomieszczenia), step=1
    )
    st.session_state.proc_swiatla = st.slider(
        "🔦 % osób, które nie gaszą światła wychodząc jako ostatnie",
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
    col_l, col_c, col_r = st.columns([1, 4, 1])
    with col_c:
        st.button("Dalej  →  Standby 🔌", key="btn_2")

# ═══════════════════════════════════════════════════════════════
# TAB 3 – STANDBY
# ═══════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="section-title">🔌 Tryb czuwania – Standby</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tip-box">
        Komputery, tablice multimedialne i rzutniki pozostawione włączone
        podczas przerw pobierają prąd bez żadnej potrzeby.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.urzadzenia = st.slider(
        "🖥️ Liczba urządzeń (komputery, tablice, rzutniki…)",
        min_value=5, max_value=400,
        value=int(st.session_state.urzadzenia), step=1
    )
    st.session_state.proc_standby = st.slider(
        "🔴 % urządzeń pozostawionych włączonych podczas przerw",
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
    col_l, col_c, col_r = st.columns([1, 4, 1])
    with col_c:
        st.button("Dalej  →  Ogrzewanie 🔥", key="btn_3")

# ═══════════════════════════════════════════════════════════════
# TAB 4 – OGRZEWANIE
# ═══════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="section-title">🔥 Ogrzewanie</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tip-box">
        Nieprawidłowe wietrzenie – zbyt długo lub przy szeroko otwartych oknach –
        powoduje ogromne straty ciepła w zimnych miesiącach.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.wietrzenia_dzien = st.slider(
        "🌬️ Średnia liczba wietrzeń sali dziennie (zimne miesiące)",
        min_value=1, max_value=15,
        value=int(st.session_state.wietrzenia_dzien), step=1
    )
    st.session_state.proc_wietrzenie = st.slider(
        "❌ % nauczycieli wietrzących salę nieprawidłowo",
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
    col_l, col_c, col_r = st.columns([1, 4, 1])
    with col_c:
        st.button("Dalej  →  Wyniki 📊", key="btn_4")

# ═══════════════════════════════════════════════════════════════
# TAB 5 – WYNIKI
# ═══════════════════════════════════════════════════════════════
with tab5:
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
    _total_zl  = _s_zl + _sb_zl + _c_zl

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

    # Łączny koszt
    total_str = f"{_total_zl:,.0f}".replace(",", "\u202f")
    st.markdown(f"""
    <div class="total-card">
        <div class="tlabel">💰 Łączny koszt zmarnowanej energii rocznie</div>
        <div class="tvalue">{total_str} zł</div>
        <div class="tsub">{_total_kwh:.0f} kWh energii elektrycznej &nbsp;+&nbsp; {_c_gj:.1f} GJ ciepła</div>
    </div>
    """, unsafe_allow_html=True)

    # Porównania
    st.markdown('<div class="section-title">🌍 To tyle samo co…</div>', unsafe_allow_html=True)

    co2_kg    = _total_kwh * 0.75
    drzewa    = max(1, int(co2_kg / 22))
    co2_tony  = round(co2_kg / 1000, 2)
    ton_wegla = round(_total_kwh * 0.00034, 2)
    km_auto   = int(_total_kwh * 6.5)
    rolki     = int(_total_kwh * 100)

    comparisons = [
        ("🌳", f"{drzewa} drzew",        "tyle drzew musiałoby rosnąć rok, by pochłonąć tyle CO₂"),
        ("☁️", f"{co2_tony} t CO₂",       "tyle dwutlenku węgla zostało wyemitowane"),
        ("⚫", f"{ton_wegla} t węgla",     "tyle węgla spalono, by wyprodukować tę energię"),
        ("🚗", f"{km_auto:,} km".replace(",", "\u202f"), "tyle kilometrów przejechałby samochód"),
        ("🧻", f"{rolki:,} rolek".replace(",", "\u202f"), "tyle rolek papieru toaletowego można by wyprodukować"),
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



