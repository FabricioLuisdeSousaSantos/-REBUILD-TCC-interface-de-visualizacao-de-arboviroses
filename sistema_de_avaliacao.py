#---------------------------------------
#  streamlit run sistema_de_avaliacao.py
#---------------------------------------

import streamlit as st
import pandas as pd
from datetime import date
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
from baixar_dados import baixar_dados
from atualizar_modelo import atualizar_modelo
from previsao import previsao

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
    with st.spinner("Checando por novos dados..."):
        baixar_dados()
    pkl_modelo = modelos[modelo]
    pkl_modelo = pkl_modelo["obj_modelo"]
    if modelo == "Dengue":
        print("dengue")
        dados_novos = pd.read_csv("./modelos/dataset_atual/dengue_tratado.csv",
        parse_dates=["data_iniSE"],
        index_col="data_iniSE").sort_index()
        caminho_modelo = "./modelos/sarimax_dengue.pkl"
        with st.spinner("Atualizando modelo..."):
            atualizado = atualizar_modelo(pkl_modelo, dados_novos, caminho_modelo)
            if atualizado:
                print("sim")
                st.success("Modelo atualizado!")
                resultados = previsao(pkl_modelo, dados_novos)
            else:
                print("não")
                st.success("O modelo já está atualizado!")
                resultados = previsao(pkl_modelo, dados_novos)

        with row1:
            st.write("Casos")
            st.line_chart(resultados)

    if modelo == "Chikungunya":
        print("chik")
        dados_novos = pd.read_csv("./modelos/dataset_atual/chikungunya_tratado.csv",
        parse_dates=["data_iniSE"],
        index_col="data_iniSE").sort_index()
        caminho_modelo = "modelos/sarimax_chik.pkl"
        with st.spinner("Atualizando modelo..."):
            atualizado = atualizar_modelo(pkl_modelo, dados_novos, caminho_modelo)
            if atualizado:
                print("sim")
                st.success("Modelo atualizado!")
                resultados = previsao(pkl_modelo, dados_novos)
            else:
                print("não")
                st.success("O modelo já está atualizado!")
                resultados = previsao(pkl_modelo, dados_novos)

        with row1:
                st.write("Casos")
                st.line_chart(resultados)

    if modelo == "Zika":
        print("zika")
        dados_novos = pd.read_csv("./modelos/dataset_atual/zika_tratado.csv",
        parse_dates=["data_iniSE"],
        index_col="data_iniSE").sort_index()
        caminho_modelo = "modelos/sarimax_zika.pkl"
        with st.spinner("Atualizando modelo..."):
            atualizado = atualizar_modelo(pkl_modelo, dados_novos, caminho_modelo)
            if atualizado:
                print("sim")
                st.success("Modelo atualizado!")
                resultados = previsao(pkl_modelo, dados_novos)
            else:
                print("não")
                st.success("O modelo já está atualizado!")
                resultados = previsao(pkl_modelo, dados_novos)

        with row1:
                st.write("Casos")
                st.line_chart(resultados)

col1, col2, col3 = st.columns([1.5, 1, 1])
with col2:
    st.image("./assets/mosquito.png", width=200)

opcao = st.selectbox("Escolha uma Arbovirose", list(modelos.keys()))
modelo_selecionado = modelos[opcao]

st.button("Fazer previsão", type="primary", on_click=predicao, args=(opcao,))

row1 = st.container()
row2 = st.container()


