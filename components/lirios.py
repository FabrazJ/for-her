import streamlit as st

def render_lirios(datos):
    st.header("¿Por qué unos lirios?")
    st.markdown(datos.get('significado_lirios', 'Los lirios representan elegancia, sinceridad y momentos especiales.'))