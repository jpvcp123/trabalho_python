import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

arquivo = pd.read_csv('vendas.csv')

dias = ["Dia 1", "Dia 2", "Dia 3"]

for produto in arquivo.columns:
    dados = np.array(arquivo[produto])
    plt.plot(dias, dados, label=produto)

plt.title("Gráfico produtos")
plt.xlabel("Dias")
plt.ylabel("Quantidade de produtos")
plt.legend()
plt.show()