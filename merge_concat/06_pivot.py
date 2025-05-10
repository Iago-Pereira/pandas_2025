# %%

import pandas as pd
# %%

df = pd.read_csv("../data/homicidios_consolidado.csv", sep=";")
df.head()
# %%

df_stack = (df.set_index(["nome", "período", ])
              .stack()
              .reset_index())

df_stack.columns = ["nome", "periodo", "metrica", "valor"]

df_stack
# %%

df_pivot = (df_stack.pivot_table(values="valor",
                                index=["nome", "periodo"],
                                columns="metrica")
                    .reset_index())

df_pivot
# %%

# agregando e calculando a média por estado desconsiderando o período
df_stack.pivot_table(values="valor",
                     index=["nome"],
                     columns="metrica",
                     aggfunc="mean")
# %%
