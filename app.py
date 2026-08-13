import streamlit as st
from utils.loader import cargar_mensajes
from components.lirios import render_lirios
from components.carta import render_carta
from components.contador import render_contador

# Configuración de la página
st.set_page_config(page_title="Para ti", page_icon="🌷", layout="centered")

# Estilos visuales refinados (Tonos blancos y lilas suaves)
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

# Cargar datos
datos = cargar_mensajes()

# Título principal
st.title(f"🌷 {datos.get('titulo_principal', 'Un detalle para ti')}")
st.write("---")

# Pestañas limpias utilizando los componentes modularizados
tab1, tab2, tab3 = st.tabs(["El Detalle", "Unas palabras", "Nuestro tiempo"])

with tab1:
    render_lirios(datos)

with tab2:
    render_carta(datos)

with tab3:
    render_contador()