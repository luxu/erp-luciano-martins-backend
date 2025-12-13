import django
import os
import pandas as pd

from utils.filename_csv import load_csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'erp_luciano_martins.settings')
django.setup()

from gasto.models import Gasto

def carregar_dados_gasto_df():
    qs = Gasto.objects.values('datagasto', 'name', 'total', 'segmento__name', 'card_bank__name')
    df = pd.DataFrame(list(qs))
    return df

def dataset_completo():
    dados = load_csv()
    df = pd.DataFrame(dados, columns=['name', 'total', 'datagasto'])
    # 🔧 Transformando a coluna total: de str para decimal (de "13,58" para 13.58)
    df['total'] = df['total'].astype(str).str.replace(',', '.', regex=False).astype(float)
    # df['datagasto'] = df['datagasto'].dt.strftime('%d/%m/%Y')
    return df
