import pandas as pd
from prophet import Prophet

from utils.datasetService import dataset_completo
from utils.vetorizacaoService import vetorizacao, encode_Y
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def prints_dataset():
    df = dataset_completo()
    return df

def prints_vetorizacao():
    X_tfidf = vetorizacao()
    print(X_tfidf)

def prints_encode_Y():
    Y_encoded = encode_Y()
    print(Y_encoded)


if __name__ == "__main__":
    print("Iniciando...")
    df = dataset_completo()
    # Agrupa por mês e comércio
    df_monthly = df.groupby([pd.Grouper(key='datagasto', freq='M'),'name']).total.sum().reset_index()
    results = []
    flag = True
    for store in df_monthly['name'].unique():
        # data = df_monthly[df_monthly['name'] == store].set_index('datagasto').sort_index()['total']
        # if len(data.dropna()) > 6:
        store_data = df_monthly[df_monthly['name'] == store].copy()
        if len(store_data) > 6:  # mínimo de histórico
            try:
                # Prophet exige colunas ds/y
                store_data = store_data.rename(columns={"datagasto": "ds", "total": "y"})

                model = Prophet(
                    yearly_seasonality=True,
                    weekly_seasonality=False,
                    daily_seasonality=False,
                )
                model.fit(store_data)

                future = model.make_future_dataframe(periods=3, freq='M')
                forecast = model.predict(future)

                future_values = forecast[['ds', 'yhat']].tail(3)

                for _, row in future_values.iterrows():
                    results.append({
                        'store': store,
                        'date': row['ds'],
                        'forecast': float(row['yhat'])
                    })

                # model = ARIMA(data, order=(1, 1, 1))
                # model_fit = model.fit()
                # fc = model_fit.forecast(steps=3)
                # for date, val in fc.items():
                #     results.append({
                #         'store': store,
                #         'date': (data.index.max() + pd.DateOffset(months=int(date))).strftime("%Y-%m"),
                #         'forecast': round(val, 2)
                #     })
            except Exception as e:
                flag = False
                print(f"Erro ao processar estabelecimento {store}: {e}")
                break

    if flag:
        forecast_df = pd.DataFrame(results)
        top5 = forecast_df.sort_values(by="forecast", ascending=False).head(5)

        # Plot
        plt.figure()
        plt.bar(top5['store'], top5['forecast'])
        plt.title("Top 5 Maiores Gastos Previstos (Próximos Meses)")
        plt.xlabel("Estabelecimento")
        plt.ylabel("Valor Previsto")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Converter gráfico para base64 para exibir no template
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')
