# %%

import pandas as pd
# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%

clientes_0 = clientes[clientes["qtdePontos"] == 0]

# Criar atributo novo
clientes_0["flag_1"] = 1
clientes_0
# %%

A = [1,2]
B = A
print(f"A:{A}")
print(f"B:{B}")

B.append("fodase")
print(f"A:{A}")
print(f"B:{B}")
# %%

# Resolvendo o problema criando uma cópia
A = [1,2]
B = A.copy()
print(f"A:{A}")
print(f"B:{B}")

B.append("fodase")
print(f"A:{A}")
print(f"B:{B}")
# %%

clientes_0 = clientes[clientes["qtdePontos"] == 0].copy()

# Criar atributo novo
clientes_0["flag_1"] = 1
clientes_0
# %%
