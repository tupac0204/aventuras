import streamlit as st

# Configuración visual de la página
st.set_page_config(page_title="Terminal de Aventuras", page_icon="🕵️‍♂️")

# Estilo Dark Mode Profesional
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #2d2d2d; color: #569cd6; border: 2px solid #569cd6; font-weight: bold; font-family: 'Consolas', monospace; }
    .stButton>button:hover { background-color: #569cd6; color: white; border: 2px solid #ffffff; }
    </style>
    """, unsafe_allow_html=True)

st.title("📂 Proyecto: Protocolo_Aventura_v3.0")
st.subheader("Acceso Restringido: Alexander ➔ Sharon")

st.code("""
# ESTADO DEL SISTEMA: OPTIMIZADO
# USUARIO DETECTADO: SHARON
# OBJETIVO PRINCIPAL: ELIMINAR LA RUTINA
""", language="python")

st.write("---")
st.write("### 📜 Cláusulas del Contrato de Aventuras")
st.write("1. **Ley Anti-Aburrimiento:** Queda estrictamente prohibido tener un fin de semana normal. Si el sistema detecta rutina, se activará un plan de emergencia automático.")
st.write("2. **Salida de Zona de Confort:** La beneficiaria (Sharon) acepta que el suscriptor (Alexander) haga locuras que juró nunca hacer, siempre que sea para verla sonreír.")
3. **Cláusula de Exclusividad:** Este contrato es único e intransferible. Sharon no es una usuaria pasajera; es la administradora de todo el sistema.")
st.write("4. **Misterio Obligatorio:** Los planes se revelarán solo 24 horas antes de su ejecución para mantener el hype.")

# Botones de Interacción
if st.button("✅ ACEPTO EL CONTRATO Y EL RIESGO"):
    st.balloons()
    st.success("¡SISTEMA ACTIVADO! Prepárate para lo que viene...")
    st.write("### ⚙️ Procesando nuevas experiencias...")
    st.info("Nota: Al aceptar, has desbloqueado una versión de Alexander que hace hasta lo imposible por sorprenderte. No hay vuelta atrás.")

if st.button("❌ CANCELAR (OPCIÓN NO RECOMENDADA)"):
    st.error("ERROR CRÍTICO: El botón de cancelar ha sido bloqueado por exceso de momentos increíbles por vivir. Intenta aceptar.")

# Footer estilo código
st.markdown("<br><br>", unsafe_allow_html=True)
st.code("while(sharon_happy): \n    alexander.continue_surprising()", language="python")
