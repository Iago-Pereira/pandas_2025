# %%

import pandas as pd
# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

dfs = pd.read_html(url)
uf = dfs[1]
uf
# %%

uf.dtypes
# %%

numero = "251 529,2"

numero = float(numero.replace(" ", "").replace(",", "."))
numero
# %%

def str_to_float(x:str):
    x = float(x.replace(" ", "")
                .replace(",", ".")
                .replace("\xa0", ""))
    return x
# %%

uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)
# %%
uf.dtypes

# %%

x = "73,9 anos"

def exp_to_anos(exp:str):
    return float(exp.replace(",", ".")
                    .replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)
uf.dtypes
# %%

x = "86,9%"

def pcent_to_float(pcent:str):
    return (float(pcent.replace(",", ".")
                       .replace("%", "")))/100

uf["Alfabetização (2016)"] = uf["Alfabetização (2016)"].apply(pcent_to_float)
uf
# %%

x = "17,0‰"

def pmil_to_float(pmil:str):
    return (float(pmil.replace(",", ".")
                       .replace("‰", "")))/1000

uf["Mortalidade infantil (2016)"] = uf["Mortalidade infantil (2016)"].apply(pmil_to_float)
uf
# %%

def uf_to_regiao(uf):

    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)
uf
# %%

#Se PIB per capita > 30.000
#+
#Mort Infantil < 15 /1000
#+
#IDH (2010) > 700
#-> "Parece bom"

#Else "Não parece bom"
# %%

linha = uf.iloc[0]

(linha["PIB per capita (R$) (2015)"] > 30000 and
 linha["Mortalidade infantil (2016)"] < 15 and
 linha["IDH (2010)"] > 700)
# %%

def classifica_bom(linha):
    if (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (2016)"] < 15 and
            linha["IDH (2010)"] > 700):
        return "Bom"
    else:
        return "Ruim"
# %%

# Padrão axis=0(colunas), para aplicar nas linhas axis=1
uf["Classifica"] = uf.apply(classifica_bom, axis=1)
uf