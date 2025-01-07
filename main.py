import streamlit as st
import requests


st.set_page_config(layout="wide")

files = [
    # st.secrets['FUNZIONI'],
    st.secrets['HOME'],
]
modules = {}

for f in files:
    response = requests.get(f)
    f_name = f.split("/")[-1]
    namespace = {}
    
    exec(response.text, namespace)

    module_name = f_name.replace('.py', '')
    modules[module_name] = namespace
    
    
    
st.title("mia app")


modules['home']['mostra']()