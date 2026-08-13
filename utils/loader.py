import json
import os
import streamlit as st

@st.cache_data
def cargar_mensajes():
    ruta = os.path.join("data", "mensajes.json")
    if os.path.exists(ruta):
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}