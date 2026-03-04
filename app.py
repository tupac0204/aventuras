import streamlit as st

# Configuración visual de la página
st.set_page_config(page_title="Terminal de Aventuras", page_icon="🚀")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #2d2d2d; color: #569cd6; border: 1px solid #569cd6; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("📂 Proyecto: New_Adventures_v2.0")
st.subheader("Acceso Privado: Alexander ➔ Sharon")

st.code("""
# STATUS: INITIALIZING...
# USER_IDENTIFIED: SHARON
# OBJECTIVE: VIVIR AVENTURAS JUNTOS
""", language="python")

st.write("---")
st.write("### 📜 Términos y Condiciones")
st.write("1. **Cero Rutina:** Se prohíben los fines de semana aburridos.")
st.write("2. **Compromiso Visual:** El suscriptor (Alexander) acepta salir de su zona de confort en el primer TikTok de Sharon (Misión Salinas).")
st.write("3. **Exclusividad:** Este sistema solo corre con nosotros dos. Sharon no es 'alguien pasajero', es el proceso principal.")

# Botones interactivos
if st.button("✅ ACEPTAR CONTRATO"):
    st.balloons()
    st.success("¡CONTRATO FIRMADO DIGITALMENTE POR SHARON!")
    st.write("### Próximos pasos del sistema:")
    st.write("- 🎵 **Viernes:** Noche en el Teatro Municipal (William Luna).")
    st.write("- 🍝 **Domingo:** Optimización de Fideos Alfredo y guerra de plastilina.")
    st.write("- ❄️ **Próximamente:** Expedición a Salinas (Trend de Jayden).")

if st.button("❌ CANCELAR"):
    st.error("ERROR 404: Opción deshabilitada. No se permite cancelar aventuras con Alexander.")