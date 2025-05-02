# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %%

df = pd.read_csv("../data/clientes.csv")
df.head()
# %%

df["pontos_100"] = df["qtdePontos"] + 100
# %%

# Semelhante a utilizar um for

nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i+100)

nova_coluna 
# %%

# não são boleanos
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()
# %%

# Intersecção

df["ambosEmailTwitch"] = df["flEmail"] * df["flTwitch"]
df.head()
# %%

df["qtdeSocial"] = df["flEmail"] +	df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()
# %%

df["todasSocial"] = df["flEmail"] *	df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head()
# %%

df["qtdePontos"].describe()
# %%

df["logPontos"] = np.log(df["qtdePontos"]+1)
df["logPontos"].describe()
# %%

plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()
# %%

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()