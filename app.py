import streamlit as st
import datetime

# Configuración de la página con estética limpia
st.set_page_config(page_title="Para ti", page_icon="🌷", layout="centered")

# Estilos visuales sutiles (Tonos blancos y lilas)
st.markdown("""
    <style>
    .main {
        background-color: #f9f8fc;
    }
    h1, h2, h3 {
        color: #5c4b99;
    }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.title("🌷 Un detalle para ti")
st.write("---")

# Pestañas o secciones limpias
tab1, tab2, tab3 = st.tabs(["El Detalle", "Unas palabras", "Nuestro tiempo"])

with tab1:
    st.header("¿Por qué unos lirios?")
    st.markdown("""
    Los lirios representan elegancia, sinceridad y momentos especiales. 
    Exactamente como lo que quería regalarte hoy.
    """)

with tab2:
    st.header("Carta especial")
    st.info("Aquí puedes escribir todo lo que sientes, un mensaje largo y sincero que complemente las flores físicas.")

with tab3:
    st.header("Contador de momentos")
    # Ejemplo de cálculo de días desde una fecha especial (cambia la fecha a la vuestra)
    fecha_especial = datetime.date(2025, 1, 1) 
    dias juntos = (datetime.date.today() - fecha_especial).days
    st.metric(label="Días desde que nuestros caminos se cruzaron", value=f"{dias_juntos} días")