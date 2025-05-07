# %%

import pandas as pd
# %%

idades = [32, 44, 12, 54, 67, 32, 23, 34, 32, 12, 45, 43, 28, 73, 29]
idades = pd.Series(idades)
idades
# %%

idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe()
# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes
# %%

clientes["flTwitch"].sum()
clientes["flTwitch"].mean()
# %%

redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].mean()
# %%

filtro = clientes.dtypes == "object"

collumns_num = clientes.dtypes[~filtro].index.tolist()

clientes[collumns_num].describe()