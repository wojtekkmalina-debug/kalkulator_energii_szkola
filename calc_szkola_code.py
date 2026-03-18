import streamlit as st

st.set_page_config(page_title="EkoKalkulator Szkoły", layout="wide")
st.title("🪫 EkoKalkulator Szkoły 2026")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["💡 Oświetlenie", "🔌 Standby", "🌡️ Ogrzewanie", "🎯 Wszystko"])

with tab1:
    col1, col2 = st.columns([1,2])
    with col1:
        swiatla_pct = st.slider("💡 % sal z zapomnianym światłem", 0, 50, 20)
        godziny = st.slider("🕐 Godziny dziennie", 6, 20, 12)
    with col2:
        kwh = swiatla_pct * godziny * 0.35
        st.metric("Oszczędzasz", f"{kwh:.0f} kWh/rok")
        st.metric("💰", f"{kwh*0.95:.0f} zł")
        st.metric("🌳", f"{int(kwh*0.0042)} drzew")
        st.metric("☁️", f"{kwh*0.75:.0f} kg CO2")

with tab2:
    col1, col2 = st.columns([1,2])
    with col1:
        standby_pct = st.slider("🔌 % urządzeń na standby", 0, 100, 40)
        urzadzenia = st.slider("📱 Liczba urządzeń", 50, 500, 200)
    with col2:
        kwh = standby_pct/100 * urzadzenia * 3.65
        st.metric("Oszczędzasz", f"{kwh:.0f} kWh/rok")
        st.metric("💰", f"{kwh*0.95:.0f} zł")
        st.metric("🚗", f"{int(kwh*0.2)} km autem")
        st.metric("⚫", f"{kwh*0.0004:.1f} t węgla")

with tab3:
    col1, col2 = st.columns([1,2])
    with col1:
        okna_pct = st.slider("🪟 % dni z otwartymi oknami", 0, 30, 10)
        ucznia = st.slider("👥 Liczba uczniów", 100, 1000, 400)
    with col2:
        kwh = okna_pct/100 * ucznia * 14
        st.metric("Oszczędzasz", f"{kwh:.0f} kWh/rok")
        st.metric("💰", f"{kwh*0.95:.0f} zł")
        st.metric("🏠", f"{int(kwh/3000)} domów")
        st.metric("☁️", f"{kwh*0.75:.0f} kg CO2")

with tab4:
    st.markdown("## 🎯 PODSUMOWANIE WSZYSTKICH NAWYKÓW")
    total_kwh = 2847 + 1234 + 5600  # suma przykładowa
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("⚡ kWh/rok", f"{total_kwh:.0f}")
    col2.metric("💰 Złote", f"{total_kwh*0.95:.0f} zł")
    col3.metric("🌳 Drzewa", f"{int(total_kwh*0.0042)}")
    col4.metric("☁️ CO2", f"{total_kwh*0.75:.0f} kg")
    
    st.balloons()
    st.success("🚀 Twoja szkoła może być EkoLiderem 2026!")


