import streamlit as st

def render_carta(datos):
    st.header("Carta especial")
    carta_parrafos = datos.get('carta', ['Aquí puedes escribir tu mensaje.'])
    for parrafo in carta_parrafos:
        st.write(parrafo)