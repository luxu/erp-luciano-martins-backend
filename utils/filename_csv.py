import pandas as pd

filename = 'gastos.csv'

def load_csv():
    dados_csv = pd.read_csv(filename, parse_dates=['datagasto'])
    return dados_csv

def salvar_dados_gasto_csv(df):
    df.to_csv('gastos.csv', index=False)
