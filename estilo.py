import streamlit as st

def aplicar_estilo():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --primaria: #4f46e5;
        --primaria-escura: #3730a3;
        --fundo: #f5f7fb;
        --card: #ffffff;
        --texto: #1e293b;
        --texto-suave: #64748b;
        --borda: #e2e8f0;
        --raio: 12px;
    }

    html, body, [class*="css"], .stApp {
        font-family: 'Inter', sans-serif;
        color: var(--texto);
    }

    /* Fundo e largura do conteúdo */
    .stApp {
        background: linear-gradient(180deg, #eef2ff 0%, var(--fundo) 40%);
    }
    .block-container {
        max-width: 900px;
        padding-top: 5rem !important;
        padding-bottom: 5rem !important;
    }

    /* Esconde menu e rodapé padrão */
    #MainMenu, footer { visibility: hidden; }

    /* Rótulos dos campos */
    label, .stSelectbox label, .stNumberInput label {
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        color: var(--texto) !important;
    }

    /* Selectbox e number input */
    div[data-baseweb="select"] > div,
    .stNumberInput input {
        background: var(--card) !important;
        border: 1px solid var(--borda) !important;
        border-radius: var(--raio) !important;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
        transition: border-color .2s, box-shadow .2s;
    }
    div[data-baseweb="select"] > div:hover,
    .stNumberInput input:focus {
        border-color: var(--primaria) !important;
        box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15) !important;
    }
    .stNumberInput > div > div {
        border-radius: var(--raio) !important;
        overflow: hidden;
    }

    /* Botões (previsão e download) */
    .stButton > button,
    .stDownloadButton > button {
        background: linear-gradient(135deg, var(--primaria), var(--primaria-escura));
        color: #fff;
        border: none;
        border-radius: var(--raio);
        padding: 0.6rem 1.4rem;
        font-weight: 600;
        letter-spacing: .2px;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        transition: transform .15s, box-shadow .15s;
    }
    .stButton > button:hover,
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(79, 70, 229, 0.4);
        color: #fff;
    }
    .stButton > button:active,
    .stDownloadButton > button:active {
        transform: translateY(0);
    }

    /* Alertas (success, warning, error) */
    [data-testid="stAlert"] {
        border-radius: var(--raio);
        border: 1px solid var(--borda);
        box-shadow: 0 2px 8px rgba(15, 23, 42, 0.05);
    }

    /* Gráfico em formato de card */
    [data-testid="stVegaLiteChart"], [data-testid="stArrowVegaLiteChart"] {
        background: var(--card);
        border: 1px solid var(--borda);
        border-radius: var(--raio);
        padding: 1rem;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.06);
    }

    /* Textos pequenos (caption) */
    [data-testid="stCaptionContainer"] {
        color: var(--texto-suave);
    }

    /* Toast */
    [data-testid="stToast"] {
        border-radius: var(--raio);
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.15);
    }
    </style>
    """, unsafe_allow_html=True)

