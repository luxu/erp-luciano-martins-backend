import os
from decimal import InvalidOperation, Decimal

import django
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score





def encode():
    ...

def preparar_dados(df):
    # 🔧 Corrige a coluna total (de "13,58" para 13.58)
    df['total'] = (
        df['total']
        .astype(str)
        .str.replace(',', '.', regex=False)
        .astype(float)
    )

    # 'datagasto', 'name', 'total', 'segmento__name', 'card_bank__name'
    # Converte name em variável numérica
    encoder = LabelEncoder()
    df['name_encoded'] = encoder.fit_transform(df['name'])

    # Define features (X) e target (y)
    X = df[
        [
            'data',
            'name_encoded'
        ]
    ]
    # X = df[
    #     [
    #         'ano',
    #         'mes',
    #         'dia_semana',
    #         'name_encoded'
    #     ]
    # ]
    y = df['total']

    return X, y, encoder

def treinar_modelo(df_limpo):
    # df = carregar_dados_gasto_df()
    X, y, encoder = preparar_dados(df_limpo)

    # Divide em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normaliza (opcional, mas recomendado)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Modelo simples de regressão linear
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Avaliação
    y_pred = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Erro quadrático médio (MSE): {mse:.2f}")
    print(f"R² (coeficiente de determinação): {r2:.2f}")

    # Exemplo de previsão
    exemplo = X_test.iloc[:5]
    pred_exemplo = model.predict(scaler.transform(exemplo))
    print("\n🔍 Previsões de exemplo:")
    print(pd.DataFrame({
        'Previsto': pred_exemplo,
        'Real': y_test.iloc[:5].values
    }))


def limpar_dataframe(df, columns_remove=None, columns_numeric=None):
    """
    Limpa o DataFrame:
      - Remove colunas desnecessárias
      - Converte números (str com vírgula) para float/Decimal
    """

    # 1️⃣ Remove colunas que não serão usadas
    if columns_remove:
        df = df.drop(columns=columns_remove, errors='ignore')

    # 2️⃣ Converte colunas numéricas que vêm como string com vírgula
    if columns_numeric:
        for col in columns_numeric:
            if col in df.columns:
                # troca vírgula por ponto
                df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
                # tenta converter em Decimal, se falhar, coloca 0
                def to_decimal(x):
                    try:
                        return Decimal(x)
                    except (InvalidOperation, ValueError):
                        return Decimal('0.00')
                df[col] = df[col].apply(to_decimal)
    df['datagasto'] = pd.to_datetime(df['datagasto']).dt.strftime('%d/%m/%Y')
    df = df.rename(columns={'datagasto': 'data'})
    print(df.head())
    return df

if __name__ == "__main__":
    print("Iniciando...")
    # 'datagasto', 'name', 'total', 'segmento__name', 'card_bank__name'
    columns_remove = ['segmento__name', 'card_bank__name',]
    columns_numeric = ['total',]
    x = vetorizacao()
    print(x)
    # dados_csv= load_csv(filename)
    # dataset_completo(dados_csv)
    # df = carregar_dados_gasto_df()
    # salvar_dados_gasto_csv(df)
    # df_limpo = limpar_dataframe(
    #     df,
    #     columns_remove=columns_remove,
    #     columns_numeric=columns_numeric
    # )
    # treinar_modelo(df_limpo)
    # preparar_dados(df_limpo)
