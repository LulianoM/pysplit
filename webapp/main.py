import streamlit as st
import pages

pages.header_intro()

pages.sidebar()

file = st.file_uploader('Selecione seu arquivo hysplit para coleta dos dados e cálculo da trajetória')
    
container_button = st.container()

if container_button.button("Processar"):
    st.info("Processing...")