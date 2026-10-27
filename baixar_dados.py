import requests
import datetime
import pandas as pd 
import os
from statsmodels.tsa.statespace.sarimax import SARIMAXResults
import warnings
warnings.filterwarnings('ignore')

def carregar_dados_api_em_csv(geo_codigo, doenca,
                              semana_epidem_inicio,
                              semana_epidem_fim,
                              ano_epidem_inicio,
                              ano_epidem_fim):
  url_base = "https://info.dengue.mat.br/api/alertcity"
  parametros_requisicao = {
    "geocode": geo_codigo,
    "disease": doenca,
    "format": "csv",
    "ew_start": semana_epidem_inicio,
    "ew_end": semana_epidem_fim,
    "ey_start": ano_epidem_inicio,
    "ey_end": ano_epidem_fim}

  resposta = requests.get(url_base, params=parametros_requisicao)
  if(resposta.status_code != 200):
    print("Erro na requisição...")

  with open(f"./modelos/dataset_atual/{doenca}.csv", "w") as f:
    f.write(resposta.text)

def dados_nulos(df, coluna):
  df[coluna].fillna(df[coluna].mean(), inplace=True)

def duplicados_ordenacao_data(df):
  df = df.drop_duplicates()
  df = df.sort_values("data_iniSE")
  df["data_iniSE"] = pd.to_datetime(df["data_iniSE"])
  df = df.set_index('data_iniSE')
  df = df.asfreq('W-SUN')
  df = df.rename(columns={'umidmed': 'umidade', 'tempmed': 'temperatura', "pop":"populacao"})
  df = df.dropna()
  return df

def salvar_dataset(df, nome):
  caminho = "./modelos/dataset_atual/"
  df.to_csv(f"{caminho}/{nome}_tratado.csv", index=True)

def baixar_dados(doenca):
    carregar_dados_api_em_csv(2928703, doenca, 1, 53, 2000, datetime.date.today().strftime("%Y"))

    dados = pd.read_csv(f"./modelos/dataset_atual/{doenca}.csv", usecols=["data_iniSE", "casos", "umidmed", "tempmed", "pop"])

    for coluna in ["umidmed", "tempmed"]:
        dados_nulos(dados, coluna)

    dados = duplicados_ordenacao_data(dados)
    salvar_dataset(dados, doenca)

    os.remove(f"./modelos/dataset_atual/{doenca}.csv")
   