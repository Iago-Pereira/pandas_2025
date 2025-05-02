# %%

import pandas as pd
# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%

clientes["qtdePontos"].sort_values()
# %%

max_ponto = clientes["qtdePontos"].max()
clientes[clientes["qtdePontos"] == max_ponto]
# %%

# Ordenar de maneira crescente 
clientes.sort_values(by="qtdePontos")
# %%

# Top 5 qtdePontos
clientes.sort_values(by="qtdePontos", ascending=False).head(5)
# %%

(clientes.sort_values(by="qtdePontos", ascending=False)
    .head(5)["idCliente"])
# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533],
    }
)

brinquedo
# %%

# maior salario desempate menor idade
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])