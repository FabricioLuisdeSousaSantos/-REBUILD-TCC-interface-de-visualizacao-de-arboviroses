def calcular_incidencia(populacao, resultados):
    df = resultados.copy()
    df["incidencia_por_100k"] = (df["previsao"] / populacao * 100000).round(2)
    return df