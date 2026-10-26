#---------------------------------------
#  streamlit run sistema_de_avaliacao.py
#---------------------------------------

import streamlit as st
import pandas as pd
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

@st.cache_resource
def carregar_modelo(caminho):
    return SARIMAXResults.load(caminho)


CONFIG = {
    "Dengue": {
        "modelo": "./modelos/sarimax_dengue.pkl",
        "dados": "./modelos/dataset_atual/dengue_tratado.csv",
    },
    "Chikungunya": {
        "modelo": "./modelos/sarimax_chik.pkl",
        "dados": "./modelos/dataset_atual/chikungunya_tratado.csv",
    },
    "Zika": {
        "modelo": "./modelos/sarimax_zika.pkl",
        "dados": "./modelos/dataset_atual/zika_tratado.csv",
    },
}

def predicao(nome):
    cfg = CONFIG[nome]

    with st.spinner("Checando por novos dados..."):
        baixar_dados()

    pkl_modelo = carregar_modelo(cfg["modelo"])
    dados_novos = pd.read_csv(
        cfg["dados"],
        parse_dates=["data_iniSE"],
        index_col="data_iniSE",
    ).sort_index()

    with st.spinner("Atualizando modelo..."):
        atualizado = atualizar_modelo(pkl_modelo, dados_novos, cfg["modelo"])
        resultados = previsao(pkl_modelo, dados_novos, semanas_futuro)

    return atualizado, resultados


def limpar():
    st.session_state.pop("resultado", None)

col1, col2, col3 = st.columns([1.5, 1, 1])
with col2:
    st.image("./assets/mosquito.png", width=200)

opcao = st.selectbox(
    "Escolha uma Arbovirose",
    list(CONFIG.keys()),
    on_change=limpar,
)

semanas_futuro = st.number_input(
    "Semanas para prever",
    min_value=1,
    max_value=12,
    value=6,     
    step=1,
)

modelo_atual = carregar_modelo(CONFIG[opcao]["modelo"])
ultima_data = modelo_atual.model._index[-1]
st.caption(f"Último dado do modelo: {ultima_data:%d/%m/%Y}")

st.write("Semanas futuras selecionadas:", semanas_futuro)

if st.button("Fazer previsão", type="primary"):
    atualizado, resultados = predicao(opcao)
    st.session_state["resultado"] = {
        "opcao": opcao,
        "atualizado": atualizado,
        "dados": resultados,
    }

row1 = st.container()

res = st.session_state.get("resultado")
if res:
    with row1:
        if res["atualizado"]:
            st.success("Modelo atualizado!")
        else:
            st.success("O modelo já está atualizado!")
        st.write(f"Casos: {res['opcao']}")
        st.line_chart(res["dados"])
    csv = res["dados"].to_csv(index_label="data").encode("utf-8-sig")
    nome_arquivo = f"previsao_{res['opcao'].lower()}.csv"
    st.download_button(
        label="Salvar previsão em um arquivo CSV",
        data=csv,
        file_name=nome_arquivo,
        mime="text/csv",
        type="primary"
)