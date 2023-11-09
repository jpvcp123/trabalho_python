import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

arquivo = pd.read_csv('vendas.csv')

produtos = arquivo.columns.tolist()

medias = []

for produto in produtos:
    dados = np.array(arquivo[produto])
    media_produto = np.mean(dados)
    medias.append(media_produto)

plt.bar(produtos, medias)
plt.title("Gráfico produtos")
plt.xlabel("Produtos")
plt.ylabel("Médias")
plt.show()
