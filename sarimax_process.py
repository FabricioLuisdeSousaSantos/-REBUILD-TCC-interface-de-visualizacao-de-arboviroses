import pandas as pd

def previsao_sarimax(modelo, exogenas):
    ultima_data = modelo.model._index[-1] + pd.Timedelta(weeks=1)
    datas_futuras = pd.date_range(start=ultima_data, periods=6, freq="W-SUN")

    hist = pd.read_csv(exogenas, index_col="data_iniSE", parse_dates=["data_iniSE"])
    medias = hist[["umidade", "temperatura"]].mean()
    exog = pd.DataFrame([medias.values] * len(datas_futuras), columns=medias.index, index=datas_futuras)

    futuro = len(exog)
    previsao = modelo.get_forecast(steps=futuro, exog=exog)
    previsoes = previsao.predicted_mean
    previsoes = pd.DataFrame(previsoes.values, columns=['previsao'], index=previsoes.index)
    previsoes["previsao"] = previsoes["previsao"].clip(lower=0)
    return previsoes
    


