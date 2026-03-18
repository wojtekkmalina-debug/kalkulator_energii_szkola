import streamlit as st

st.title("🪫 Kalkulator Energii Szkoły - TEST")

# Proste suwaki
uczniowie = st.slider("Liczba uczniów", 100, 1000, 400)
swiatla = st.slider("% zapomnianych świateł", 0, 50, 20)
standby = st.slider("% urządzeń na standby", 0, 100, 40)
cena = st.number_input("Cena prądu (zł/kWh)", 0.8, 1.2, 0.95)

# BARDZO proste obliczenia testowe
kwh_rocznie = uczniowie * 40
oszczednosc_kwh = kwh_rocznie * (swiatla * 0.0025 + standby * 0.001)
zlote = oszczednosc_kwh * cena

# Wyniki w kolumnach
col1, col2, col3 = st.columns(3)
col1.metric("Oszczędzasz kWh/rok", f"{oszczednosc_kwh:.0f}")
col2.metric("Złote/rok", f"{zlote:.0f} zł")
col3.metric("Wpływ na środowisko", "🌍 Super!")

st.success("Test działa! 💚 Później ulepszymy formuły.")

