from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

from utils.datasetService import dataset_completo
from utils.filename_csv import load_csv


def vetorizacao():
    """
    X -> É a pergunta que faremos para o modelo
    Y -> É a resposta dessa pergunta
    Nome das coisas no ML
    - Resposta(Y)(Label-Target-Rótulos)
    - Pergunta(X)(Features)
    No meu caso a feature(Supermercado Nagai, Avenida) e a label nos diz qual a
    porcentagem de gastos em cada categoria.
    Qdo vetorizamos só vetorizamos o X
    """
    tfidf = TfidfVectorizer()
    df = dataset_completo()
    X = df['total']
    # fitar == treinar os dados
    tfidf.fit(X)
    # Dados vetorizados
    X_tfidf = tfidf.transform(X)
    return X_tfidf

def encode_Y():
    label_encoder = LabelEncoder()
    df = dataset_completo()

    Y = df['name'].astype(str)

    Y_encoded = label_encoder.fit_transform(Y)

    return Y_encoded

