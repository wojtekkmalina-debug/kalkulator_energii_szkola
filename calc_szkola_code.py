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

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif !important;
}

.stApp {
    background: linear-gradient(160deg, #edf9f1 0%, #d4f0e0 100%);
}

/* Ukryj domyślny header Streamlit */
#MainMenu, header, footer { visibility: hidden; }

/* Zakładki */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: #c8f0d8;
    padding: 6px;
    border-radius: 16px;
    flex-wrap: wrap;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 12px;
    padding: 6px 10px;
    font-weight: 700;
    font-size: 0.82rem;
    color: #1a4a2e;
    background: transparent;
}
.stTabs [aria-selected="true"] {
    background: #2d7a4f !important;
    color: white !important;
}

/* Przyciski */
.stButton > button {
    background: linear-gradient(135deg, #2d7a4f, #1a4a2e);
    color: white;
    border: none;
    border-radius: 14px;
    font-family: 'Nunito', sans-serif;
    font-weight: 800;
    font-size: 1.1rem;
    padding: 14px 0;
    width: 100%;
    letter-spacing: 0.03em;
    box-shadow: 0 4px 16px rgba(30,80,50,0.25);
    transition: all 0.2s;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #3d9a6f, #2d7a4f);
    box-shadow: 0 6px 20px rgba(30,80,50,0.35);
    transform: translateY(-2px);
}

/* Suwaki */
.stSlider > div > div > div > div {
    background: #2d7a4f;
}

/* Metryki */
[data-testid="stMetricValue"] {
    color: #1a4a2e;
    font-weight: 800;
    font-size: 1.4rem;
}

/* Karty info */
.info-card {
    background: white;
    border-radius: 18px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 4px 20px rgba(30,80,50,0.10);
    border-left: 5px solid #2d7a4f;
}

.welcome-card {
    background: linear-gradient(135deg, #1a4a2e, #2d7a4f);
    color: white;
    border-radius: 20px;
    padding: 28px 22px;
    margin: 16px 0;
    text-align: center;
    box-shadow: 0 6px 28px rgba(30,80,50,0.25);
}

.welcome-card h2 {
    font-size: 1.5rem;
    font-weight: 900;
    margin-bottom: 10px;
    line-height: 1.3;
}

.welcome-card p {
    font-size: 0.98rem;
    opacity: 0.9;
    line-height: 1.6;
}

.result-card {
    background: white;
    border-radius: 18px;
    padding: 18px;
    margin: 8px 0;
    box-shadow: 0 4px 18px rgba(30,80,50,0.10);
    text-align: center;
}

.result-card .label {
    font-size: 0.85rem;
    color: #4a6b54;
    font-weight: 600;
    margin-bottom: 4px;
}

.result-card .value {
    font-size: 1.6rem;
    font-weight: 900;
    color: #1a4a2e;
}

.result-card .unit {
    font-size: 0.9rem;
    color: #2d7a4f;
    font-weight: 700;
}

.compare-card {
    background: #edf9f1;
    border-radius: 14px;
    padding: 14px 16px;
    margin: 6px 0;
    display: flex;
    align-items: center;
    gap: 12px;
    border: 1.5px solid #c8f0d8;
}

.section-title {
    font-size: 1.25rem;
    font-weight: 900;
    color: #1a4a2e;
    margin: 16px 0 10px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.tip-box {
    background: #f0fdf4;
    border: 1.5px dashed #2d7a4f;
    border-radius: 14px;
    padding: 14px;
    margin: 12px 0;
    font-size: 0.9rem;
    color: #1a4a2e;
}
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────
defaults = {
    'sale_lekcyjne': 25,
    'przerwy_godz': 1.67,
    'cena_pradu': 0.95,
    'cena_ciepla': 68.0,
    'inne_pomieszczenia': 12,
    'proc_swiatla': 30,
    'urzadzenia': 55,
    'proc_standby': 35,
    'wietrzenia_dzien': 4,
    'proc_wietrzenie': 40,
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
    "📊 Wyniki"
])

# ══════════════════════════════════════════════════════════════
# TAB 1 – POWITANIE + SUWAKI BAZOWE
# ══════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="welcome-card">
        <div style="font-size:2.8rem; margin-bottom:10px;">🌿</div>
        <h2>Cześć! Witaj w EkoKalkulatorze</h2>
        <p>
            Oto EkoKalkulator stworzony na potrzeby konkursu
            <strong>„Zasil Szkołę Pomysłem"</strong> przez zespół
            <strong>Prądziaki</strong> z III LO im. Mikoła Słowaka w Chorzowie.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card">
        <b>📋 Skąd pochodzą dane?</b><br><br>
        Wszystkie wartości domyślne zostały zebrane przez nas bezpośrednio
        w naszej szkole. Przesuwając suwaki, możesz jednak łatwo dostosować
        kalkulator do <b>dowolnej innej szkoły</b> i sprawdzić, ile energii
        marnuje się właśnie tam.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">⚙️ Dane podstawowe szkoły</div>', unsafe_allow_html=True)

    st.session_state.sale_lekcyjne = st.slider(
        "🏫 Liczba sal lekcyjnych",
        min_value=5, max_value=60, value=st.session_state.sale_lekcyjne, step=1
    )
    st.session_state.przerwy_godz = st.slider(
        "⏱️ Łączny czas przerw w ciągu dnia (godz.)",
        min_value=0.5, max_value=4.0, value=st.session_state.przerwy_godz, step=0.05,
        format="%.2f h"
    )
    st.session_state.cena_pradu = st.slider(
        "⚡ Aktualna cena prądu (zł/kWh)",
        min_value=0.50, max_value=1.50, value=st.session_state.cena_pradu, step=0.01,
        format="%.2f zł"
    )
    st.session_state.cena_ciepla = st.slider(
        f"🔥 Aktualna cena energii cieplnej (zł/GJ)  *(cena na dzień {today})*",
        min_value=20.0, max_value=150.0, value=st.session_state.cena_ciepla, step=0.5,
        format="%.1f zł"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("➡️ Dalej – Oświetlenie"):
        st.info("✅ Przejdź do zakładki **💡 Oświetlenie** na górze strony.")

# ══════════════════════════════════════════════════════════════
# TAB 2 – OŚWIETLENIE
# ══════════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-title">💡 Oświetlenie</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
        Ile światła pali się niepotrzebnie podczas przerw?
        Uwzględniamy zarówno sale lekcyjne, jak i inne pomieszczenia.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.inne_pomieszczenia = st.slider(
        "🚻 Liczba innych pomieszczeń (toalety, szatnie, korytarze…)",
        min_value=1, max_value=40, value=st.session_state.inne_pomieszczenia, step=1
    )
    st.session_state.proc_swiatla = st.slider(
        "🔦 Odsetek osób, które nie gaszą światła wychodząc ostatnie (%)",
        min_value=0, max_value=100, value=st.session_state.proc_swiatla, step=1,
        format="%d%%"
    )

    # OBLICZENIA
    strata_swiatlo_kwh = (
        (st.session_state.sale_lekcyjne + st.session_state.inne_pomieszczenia)
        * st.session_state.przerwy_godz
        * 0.5
        * (st.session_state.proc_swiatla / 100)
        * 180
    )
    strata_swiatlo_zl = strata_swiatlo_kwh * st.session_state.cena_pradu

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">Marnowana energia rocznie</div>
            <div class="value">{strata_swiatlo_kwh:.0f}</div>
            <div class="unit">kWh / rok</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">Koszt zmarnowanej energii</div>
            <div class="value">{strata_swiatlo_zl:.0f}</div>
            <div class="unit">zł / rok</div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("➡️ Dalej – Standby"):
        st.info("✅ Przejdź do zakładki **🔌 Standby** na górze strony.")

# ══════════════════════════════════════════════════════════════
# TAB 3 – STANDBY
# ══════════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="section-title">🔌 Tryb czuwania (Standby)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
        Komputery, tablice multimedialne i rzutniki pozostawione włączone
        podczas przerw pobierają energię zupełnie bez potrzeby.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.urzadzenia = st.slider(
        "🖥️ Łączna liczba urządzeń (komputery, tablice, rzutniki…)",
        min_value=5, max_value=200, value=st.session_state.urzadzenia, step=1
    )
    st.session_state.proc_standby = st.slider(
        "🔴 Odsetek urządzeń pozostawionych włączonych podczas przerw (%)",
        min_value=0, max_value=100, value=st.session_state.proc_standby, step=1,
        format="%d%%"
    )

    # OBLICZENIA
    strata_standby_kwh = (
        st.session_state.urzadzenia
        * st.session_state.przerwy_godz
        * (st.session_state.proc_standby / 100)
        * 0.2
        * 180
    )
    strata_standby_zl = strata_standby_kwh * st.session_state.cena_pradu

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">Marnowana energia rocznie</div>
            <div class="value">{strata_standby_kwh:.0f}</div>
            <div class="unit">kWh / rok</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">Koszt zmarnowanej energii</div>
            <div class="value">{strata_standby_zl:.0f}</div>
            <div class="unit">zł / rok</div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("➡️ Dalej – Ogrzewanie"):
        st.info("✅ Przejdź do zakładki **🔥 Ogrzewanie** na górze strony.")

# ══════════════════════════════════════════════════════════════
# TAB 4 – OGRZEWANIE
# ══════════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="section-title">🔥 Ogrzewanie</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
        Nieprawidłowe wietrzenie (zbyt długo, zbyt szeroko otwarte okna)
        powoduje ogromne straty ciepła w zimnych miesiącach.
    </div>
    """, unsafe_allow_html=True)

    st.session_state.wietrzenia_dzien = st.slider(
        "🌬️ Średnia liczba wietrzeń sali dziennie (w zimnych miesiącach)",
        min_value=1, max_value=15, value=st.session_state.wietrzenia_dzien, step=1
    )
    st.session_state.proc_wietrzenie = st.slider(
        "❌ Odsetek nauczycieli wietrzących salę nieprawidłowo (%)",
        min_value=0, max_value=100, value=st.session_state.proc_wietrzenie, step=1,
        format="%d%%"
    )

    # OBLICZENIA
    # cena_ciepla jest w zł/GJ, wzór: cena[zł/GJ] * sale * % * 0.005[GJ] * wietrzenia * 180
    strata_cieplo_gj = (
        st.session_state.cena_ciepla   # zł/GJ – używamy jako GJ/zł w jednostkach straty GJ
        * st.session_state.sale_lekcyjne
        * (st.session_state.proc_wietrzenie / 100)
        * 0.005
        * st.session_state.wietrzenia_dzien
        * 180
    )
    # Wartość w GJ (bez ceny):
    strata_cieplo_gj_ilosc = (
        st.session_state.sale_lekcyjne
        * (st.session_state.proc_wietrzenie / 100)
        * 0.005
        * st.session_state.wietrzenia_dzien
        * 180
    )
    strata_cieplo_zl = strata_cieplo_gj_ilosc * st.session_state.cena_ciepla

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">Marnowane ciepło rocznie</div>
            <div class="value">{strata_cieplo_gj_ilosc:.2f}</div>
            <div class="unit">GJ / rok</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">Koszt zmarnowanego ciepła</div>
            <div class="value">{strata_cieplo_zl:.0f}</div>
            <div class="unit">zł / rok</div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("➡️ Zobacz Wyniki"):
        st.info("✅ Przejdź do zakładki **📊 Wyniki** na górze strony.")

# ══════════════════════════════════════════════════════════════
# TAB 5 – WYNIKI
# ══════════════════════════════════════════════════════════════
with tab5:
    # Przeliczamy wszystko od nowa (na wypadek gdy user wejdzie tu bezpośrednio)
    _swiatlo_kwh = (
        (st.session_state.sale_lekcyjne + st.session_state.inne_pomieszczenia)
        * st.session_state.przerwy_godz
        * 0.5
        * (st.session_state.proc_swiatla / 100)
        * 180
    )
    _swiatlo_zl = _swiatlo_kwh * st.session_state.cena_pradu

    _standby_kwh = (
        st.session_state.urzadzenia
        * st.session_state.przerwy_godz
        * (st.session_state.proc_standby / 100)
        * 0.2
        * 180
    )
    _standby_zl = _standby_kwh * st.session_state.cena_pradu

    _cieplo_gj = (
        st.session_state.sale_lekcyjne
        * (st.session_state.proc_wietrzenie / 100)
        * 0.005
        * st.session_state.wietrzenia_dzien
        * 180
    )
    _cieplo_zl = _cieplo_gj * st.session_state.cena_ciepla

    _total_kwh = _swiatlo_kwh + _standby_kwh
    _total_zl = _swiatlo_zl + _standby_zl + _cieplo_zl

    st.markdown('<div class="section-title">📊 Podsumowanie roczne</div>', unsafe_allow_html=True)

    # ── Energia elektryczna ──
    st.markdown("#### ⚡ Energia elektryczna")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">💡 Oświetlenie – energia</div>
            <div class="value">{_swiatlo_kwh:.0f}</div>
            <div class="unit">kWh / rok</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">💡 Oświetlenie – koszt</div>
            <div class="value">{_swiatlo_zl:.0f}</div>
            <div class="unit">zł / rok</div>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">🔌 Standby – energia</div>
            <div class="value">{_standby_kwh:.0f}</div>
            <div class="unit">kWh / rok</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">🔌 Standby – koszt</div>
            <div class="value">{_standby_zl:.0f}</div>
            <div class="unit">zł / rok</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Energia cieplna ──
    st.markdown("#### 🔥 Energia cieplna")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">🔥 Ogrzewanie – straty</div>
            <div class="value">{_cieplo_gj:.2f}</div>
            <div class="unit">GJ / rok</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="result-card">
            <div class="label">🔥 Ogrzewanie – koszt</div>
            <div class="value">{_cieplo_zl:.0f}</div>
            <div class="unit">zł / rok</div>
        </div>
        """, unsafe_allow_html=True)

    # ── SUMA ──
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1a4a2e, #2d7a4f);
                border-radius: 20px; padding: 24px; text-align: center;
                color: white; margin: 8px 0 20px 0;
                box-shadow: 0 6px 28px rgba(30,80,50,0.3);">
        <div style="font-size:0.95rem; opacity:0.85; margin-bottom:6px; font-weight:600;">
            💰 ŁĄCZNY KOSZT ZMARNOWANEJ ENERGII ROCZNIE
        </div>
        <div style="font-size:2.8rem; font-weight:900; letter-spacing:-0.01em;">
            {_total_zl:.0f} zł
        </div>
        <div style="font-size:0.9rem; opacity:0.75; margin-top:6px;">
            w tym {_total_kwh:.0f} kWh energii elektrycznej + {_cieplo_gj:.2f} GJ ciepła
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── PORÓWNANIA ──
    st.markdown('<div class="section-title">🌍 To tyle samo co…</div>', unsafe_allow_html=True)

    drzewa     = max(1, int(_total_kwh / 0.02 / 1000 * 0.5))   # ~1 drzewo pochłania ~22 kg CO₂/rok
    co2_tony   = round(_total_kwh * 0.75 / 1000, 2)
    ton_wegla  = round(_total_kwh * 0.00034, 2)
    km_auto    = int(_total_kwh * 6.5)
    rolki      = int(_total_kwh * 100)

    comparisons = [
        ("🌳", f"{drzewa} drzew", "tyle drzew musiałoby rosnąć rok, by pochłonąć tyle CO₂"),
        ("☁️", f"{co2_tony} ton CO₂", "tyle dwutlenku węgla zostało wyemitowane"),
        ("⚫", f"{ton_wegla} ton węgla", "tyle węgla spalono, by wyprodukować tę energię"),
        ("🚗", f"{km_auto:,} km".replace(",", " "), "tyle kilometrów przejechałoby auto spalając tę energię"),
        ("🧻", f"{rolki:,} rolek".replace(",", " "), "tyle rolek papieru toaletowego można by wyprodukować"),
    ]

    for icon, value, desc in comparisons:
        st.markdown(f"""
        <div style="background: white; border-radius: 14px; padding: 14px 16px;
                    margin: 6px 0; display: flex; align-items: center; gap: 14px;
                    box-shadow: 0 2px 12px rgba(30,80,50,0.08);
                    border-left: 4px solid #4caf78;">
            <div style="font-size:1.8rem; min-width:36px; text-align:center;">{icon}</div>
            <div>
                <div style="font-size:1.2rem; font-weight:900; color:#1a4a2e;">{value}</div>
                <div style="font-size:0.82rem; color:#4a6b54; margin-top:2px;">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: #f0fdf4; border: 2px solid #4caf78; border-radius: 16px;
                padding: 18px; text-align: center; margin-top: 8px;">
        <div style="font-size:1.4rem;">💚</div>
        <div style="font-weight:800; color:#1a4a2e; font-size:1rem; margin-top:6px;">
            Zmieniając codzienne nawyki, wasza szkoła może zaoszczędzić<br>
            energię i pieniądze – oraz pomóc planecie!
        </div>
        <div style="font-size:0.82rem; color:#4a6b54; margin-top:8px;">
            EkoKalkulator – Prądziaki | III LO im. M. Słowaka w Chorzowie
        </div>
    </div>
    """, unsafe_allow_html=True)


