# -*- coding: utf-8 -*-
"""
DGT2823 - Tecnologias para desenvolvimento de soluções de big data
Trabalho Prático: limpeza de dados com Pandas
"""
import pandas as pd

# ============================================================
# MICROATIVIDADE 1 - Ler um arquivo CSV
# ============================================================
# sep=';'       -> separador de colunas
# engine='python' -> engine pedida no enunciado
# quotechar="'" -> as datas no arquivo vêm entre aspas simples ('2020/12/01');
#                  assim as aspas são removidas e o valor fica 2020/12/01
df = pd.read_csv("dados.csv", sep=";", engine="python",
                 encoding="utf-8", quotechar="'")
print("=== MICROATIVIDADE 1: dados lidos ===")
print(df)

# ============================================================
# MICROATIVIDADE 2 - Subconjunto de dados (3 colunas)
# ============================================================
subconjunto = df[["ID", "Duration", "Calories"]]
print("\n=== MICROATIVIDADE 2: subconjunto (3 colunas) ===")
print(subconjunto)

# ============================================================
# MICROATIVIDADE 3 - Configurar max_rows e usar to_string()
# ============================================================
pd.set_option("display.max_rows", 9999)
print("\n=== MICROATIVIDADE 3: dataset completo com to_string() ===")
print(df.to_string())

# ============================================================
# MICROATIVIDADE 4 - Primeiras e últimas N linhas
# ============================================================
print("\n=== MICROATIVIDADE 4: primeiras 10 linhas ===")
print(df.head(10))
print("\n=== MICROATIVIDADE 4: últimas 10 linhas ===")
print(df.tail(10))

# ============================================================
# MICROATIVIDADE 5 - Informações gerais (info)
# ============================================================
print("\n=== MICROATIVIDADE 5: info() ===")
df.info()
# Do info() tiramos: total de linhas (RangeIndex), total de colunas,
# nulos (Non-Null Count), tipo (Dtype) e memória utilizada (memory usage).

# ============================================================
# TRABALHO PRÁTICO
# ============================================================
print("\n" + "=" * 60)
print("TRABALHO PRÁTICO")
print("=" * 60)

# Passos 1-4: leitura (feita acima) + verificação
print("\n--- Informações gerais ---")
df.info()
print("\n--- Primeiras 5 linhas ---")
print(df.head())
print("\n--- Últimas 5 linhas ---")
print(df.tail())

# Passo 5: cópia do dataset original
df_limpo = df.copy()

# Passo 6: nulos de 'Calories' -> 0
df_limpo["Calories"] = df_limpo["Calories"].fillna(0)
print("\n--- Após substituir nulos de Calories por 0 ---")
print(df_limpo.to_string())

# Passo 7: nulos de 'Date' -> '1900/01/01'
df_limpo["Date"] = df_limpo["Date"].fillna("1900/01/01")
print("\n--- Após substituir nulos de Date por '1900/01/01' ---")
print(df_limpo.to_string())

# Passo 8: tentativa de converter 'Date' para datetime (pode gerar erro)
try:
    df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
except Exception as e:
    print("\n[ERRO ESPERADO - passo 8]:", e)

# Passo 9: trocar '1900/01/01' por NaN e tentar de novo
df_limpo["Date"] = df_limpo["Date"].replace("1900/01/01", float("nan"))
try:
    df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
except Exception as e:
    print("\n[ERRO ESPERADO - passo 9]:", e)
print("\n--- Após passo 9 ---")
print(df_limpo.to_string())

# Passo 10: corrigir especificamente o valor '20201226'
# to_datetime interpreta o valor no formato %Y%m%d; strftime o devolve como
# '2020/12/26' (padrão das demais linhas); replace troca só esse valor.
valor_correto = pd.to_datetime("20201226", format="%Y%m%d").strftime("%Y/%m/%d")
df_limpo["Date"] = df_limpo["Date"].replace("20201226", valor_correto)

# Passo 11: converter toda a coluna 'Date' para datetime
df_limpo["Date"] = pd.to_datetime(df_limpo["Date"], format="%Y/%m/%d")
print("\n--- Após converter toda a coluna Date para datetime ---")
print(df_limpo.to_string())

# Passo 12: remover registros com valor nulo em 'Date' (linha 22)
df_limpo = df_limpo.dropna(subset=["Date"])

# Passo 13: resultado final
print("\n--- DATAFRAME FINAL ---")
print(df_limpo.to_string())
print("\n--- info() final ---")
df_limpo.info()
