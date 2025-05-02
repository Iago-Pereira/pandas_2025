# %%

import pandas as pd
# %%

df = pd.read_csv("../data/transacoes.csv")
df.head()
# %%

df.shape
# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%

renamed_columns = {
                    "qtdePontos": "qtPontos",
                    "descSistemaOrigem": "SistemaOrigem"
                    }

# df = df.rename(columns=renamed_columns)
df.rename(columns=renamed_columns, inplace=True) # não é necessário atribuir ao df novamente
# %%

df.head()
# %%

colunas = ["idCliente", "qtPontos"]

df[colunas]
# %%

# SELECT * FROM df
df
# %%

# SELECT idCliente FROM df
df[["idCliente"]]
# %%

# SELECT idCliente, qtPontos FROM df LIMIT 5
df[["idCliente", "qtPontos"]].sample(5)
# %%

# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5
df[["idCliente", "idTransacao", "qtPontos"]].head(5)
# %%

# Colunas na ordem alfabética
colunas = df.columns.tolist()
colunas.sort()
colunas

df = df[colunas]
df.head()