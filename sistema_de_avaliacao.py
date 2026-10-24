#---------------------------------------
#  streamlit run sistema_de_avaliacao.py
#---------------------------------------

import streamlit as st
import pandas as pd
from datetime import date
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
from sarimax_process import previsao_sarimax
from api_info_dengue import atualizar_modelo

st.set_page_config(
    page_title="Sistema de Avaliação de Arboviroses",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="./assets/mosquito.png"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }

    div.stButton > button:first-child {
        background-color: #203366;
        color: white;
        border: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #909ed0;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

dengue = SARIMAXResults.load('./modelos/sarimax_dengue.pkl')
chikugunya = SARIMAXResults.load('./modelos/sarimax_chik.pkl')
zika = SARIMAXResults.load('./modelos/sarimax_zika.pkl')

modelos = {
    "Dengue": {"obj_modelo": dengue, 
               "caminho": "./modelos/sarimax_dengue.pkl"},


    "Chikungunya": {"obj_modelo": chikugunya, 
               "caminho": "./modelos/sarimax_chik.pkl"},


    "Zika": {"obj_modelo": zika, 
               "caminho": "./modelos/sarimax_zika.pkl"},
}

def predicao(modelo):
    modelo_treinado = modelos[modelo]
    dados_novos = atualizar_modelo(modelo_treinado, modelo_treinado["obj_modelo"], modelo_treinado["caminho"])
    resultado_casos = previsao_sarimax(modelo_treinado, dados_novos[["umidade", "temperatura"]])
    print(resultado_casos["previsao"])
    with row1:
        st.write("Casos")
        st.line_chart(resultado_casos)

col1, col2, col3 = st.columns([1.5, 1, 1])
with col2:
    st.image("./assets/mosquito.png", width=200)

opcao = st.selectbox("Escolha uma Arbovirose", list(modelos.keys()))
modelo_selecionado = modelos[opcao]

st.button("Fazer previsão", type="primary", on_click=predicao, args=(opcao,))

row1 = st.container()
row2 = st.container()


