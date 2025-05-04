# %%
# Selecione a primeira transação diária de cada cliente

import pandas as pd
# %%

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head(5)
# %%

transacoes = transacoes.sort_values("dtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])
# %%
# intervalo entre a primeira e a última transação

transacoes = transacoes.sort_values("dtCriacao")

first = transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])
last = transacoes.drop_duplicates(keep="last", subset=["idCliente", "data"])

pd.concat([last, first])