# %%

import pandas as pd
# %%

dfs = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")
dfs
# %%

type(dfs)
# %%

dfs[1]
# %%

df_uf = dfs[1]
df_uf.to_csv("df_uf.csv", index=False, sep=",")