# %%

import pandas as pd

# %%
df = pd.read_csv("../data/transacao_produto.csv")
df
# %%

df[(df["idProduto"] == 5) | (df["idProduto"] == 11)]
# %%

# Mesma lógica
df[df["idProduto"].isin([5, 11])]
# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%

# Data de criação não nula
clientes[clientes["dtCriacao"].notna()]
# %%

# Mesma lógica
clientes[~clientes["dtCriacao"].isna()]