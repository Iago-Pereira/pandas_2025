# %%

import pandas as pd
# %%

df = pd.read_csv("../data/clientes.csv")
df.head()
# %%

# Selecionando apenas um trecho do idCliente
idCliente = "000ff655-fa9f-4baa-a108-47f581ec52a1"

def get_last_id(idCliente):
    return idCliente.split("-")[-1]
# %%

get_last_id("000ff655-fa9f-4baa-a108-47f581ec52a1")
# %%

id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()
# %%

# Utilizando o método apply

df["idCliente"].apply(get_last_id)