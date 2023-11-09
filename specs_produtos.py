import pandas as pd
import numpy as np

arquivo = pd.read_csv('vendas.csv')

count = 0

for produto in arquivo.columns:
    dados = np.array(arquivo[produto])
    medias = np.mean(dados)
    mediana = np.median(dados)
    desvio_padrao = np.std(dados)
    print(f"A media do produto {count+1} é {medias}, a mediana é {mediana}, e o desvião padrão é {desvio_padrao}")
    count = count+1