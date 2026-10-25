import pandas as pd
def atualizar_modelo(modelo, dados_novos, caminho_modelo):
    ultima = modelo.model._index[-1]           
    proxima_semana = ultima + pd.Timedelta(weeks=1)
    novos = dados_novos.loc[dados_novos.index >= proxima_semana]
    if novos.empty:
        return False
    else:
        modelo = modelo.append(novos["casos"], exog=novos[["umidade", "temperatura"]], refit=False)
        modelo.save(caminho_modelo)
    return True
   