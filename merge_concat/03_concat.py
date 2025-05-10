# %%

import pandas as pd
# %%

df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})

df2 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["kozato", "laura", "dan"],
    "idade": [32,29,31],
})

df3 = pd.DataFrame({
    "idade": [32,34,19,54,33],
})
# %%

dfs = [df, df2]

pd.concat(dfs, ignore_index=True)
# %%

df3 = df3.sort_values(by='idade').reset_index(drop=True)
df3
# %%

pd.concat([df, df3], axis=1)
# %%
