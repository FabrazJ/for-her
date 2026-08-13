import streamlit as st
import datetime

def render_contador():
    st.header("Contador de momentos")
    # Cambia esta fecha a la vuestra (Año, Mes, Día)
    fecha_especial = datetime.date(2025, 1, 1) 
    dias_juntos = (datetime.date.today() - fecha_especial).days
    st.metric(label="Días desde que nuestros caminos se cruzaron", value=f"{dias_juntos} días")