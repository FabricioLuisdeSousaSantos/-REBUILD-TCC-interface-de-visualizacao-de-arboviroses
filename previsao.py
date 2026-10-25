import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def previsao(modelo, dados_novos):
    ultima_data = modelo.model._index[-1] + pd.Timedelta(weeks=1)
    datas_futuras = pd.date_range(start=ultima_data, periods=12, freq="W-SUN")

    medias = dados_novos[["umidade", "temperatura"]].mean()
    exog = pd.DataFrame([medias.values] * len(datas_futuras), columns=medias.index, index=datas_futuras)
    print("===============")
    print(ultima_data)
    print(datas_futuras)
    print(exog)

    futuro = len(exog)
    previsao = modelo.get_forecast(steps=len(datas_futuras), exog=exog)
    previsoes = previsao.predicted_mean
    previsoes = pd.DataFrame(previsoes.values, columns=['previsao'], index=previsoes.index)
    previsoes["previsao"] = previsoes["previsao"].clip(lower=0)
    print(previsao)
    return previsoes