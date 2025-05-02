# %%

import pandas as pd
# %%

df = pd.read_csv("../data/transacoes.csv")
df.head()

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
    
print(f"Valores >= 50: {resultado}")
print(f"Filtro boleano: {filtro}")
# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [ 32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)

filtro = brinquedo["idade"] >= 18

brinquedo[filtro]
# %%

df = pd.read_csv("../data/transacoes.csv")
df.head()

 # Valores maiores que 50
df[df["qtdePontos"] >= 50]
# %%

# Valores entre 50 (inclusive) e 100
df[(df["qtdePontos"] >= 50) & (df["qtdePontos"] < 100)]
# %%

# Valores iguais a 1 ou a 100
df[(df["qtdePontos"] == 1) | (df["qtdePontos"] == 100)]

# %%

# Valores entre 0 a 50(inclusive) ou a partir de 2025
df[(df["qtdePontos"] > 0) & (df["qtdePontos"] <= 50) | (df["dtCriacao"] >= '2025-01-01')]
# %%

