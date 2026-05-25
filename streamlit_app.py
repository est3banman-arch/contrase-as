import streamlit as st
import requests
from config import API_BASE_URL 

def panel_administrador():

    st.set_page_config(page_title="Contraseñas")
    
    st.markdown("""
        <style>
            header[data-testid="stHeader"] {
            opacity: 0; 
            /*visibility: hidden;*/
            transition: opacity .3s ease;
        }

        header[data-testid="stHeader"]:hover {
            opacity: 1;
        }    
                
        [data-testid="stWidgetLabel"] p{
            font-size: 22px; 
        }
        [data-testid="stTextInputRootElement"] {
            height: 50px; 
        }
        [data-testid="stTextInputRootElement"] input{
            font-size: 23px;  
        }
        </style>
    """,unsafe_allow_html=True)

    st.header("🔐 Nueva Contraseña", divider="rainbow", text_alignment="center")

    # El formulario visual
    with st.form("form_registro_claves", clear_on_submit=True):
        username = st.text_input("Nombre de Usuario")
        
        password = st.text_input("Nueva Contraseña", type="password")
        
        password_confirm = st.text_input("Repetir Contraseña", type="password")
            
        submit = st.form_submit_button("Guardar Contraseña", type="primary")

    if submit:
        if not username or not password:
            st.warning("⚠️ Debes rellenar el usuario y la contraseña.")
            return
            
        if password != password_confirm:
            st.error("❌ Las contraseñas no coinciden.")
            return

        datos_registro = {
            "username": username,
            "password": password
        }
        
        url_api = f"{API_BASE_URL}/admin/registro-clave"
        
        try:
            respuesta = requests.post(url_api, json=datos_registro)
            
            if respuesta.status_code == 200:
                mensaje = respuesta.json().get("mensaje")
                st.success(f"✅ ¡Éxito! {mensaje}")
                st.balloons()
            else:
                error = respuesta.json().get("detail", "Error desconocido")
                st.error(f"❌ Error de la API: {error}")
                
        except requests.exceptions.ConnectionError:
            st.error("❌ No se pudo conectar con la API. ¿Está Uvicorn encendido?")


panel_administrador()
