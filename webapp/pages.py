import streamlit as st

def header_intro():
    st.header("PySplit - Trajectory Generator")
    st.text('version 0 - Last update 25/07/2023')


def sidebar():
    #Créditos
    st.sidebar.write('Docs:')
    st.sidebar.markdown("[![Documentation](https://i.stack.imgur.com/tskMh.png) Docs](https://github.com/LulianoM/pysplit-ptbr)")
    st.sidebar.write('Contact:')
    st.sidebar.markdown("[![GitHub](https://i.stack.imgur.com/tskMh.png) Github](https://github.com/LulianoM)")
    st.sidebar.markdown("[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/lulianom/)")