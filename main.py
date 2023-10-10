from flask import Flask, request, render_template, redirect, url_for
import numpy as np
from prediction import sales_prediction
from forecast import forecast_nation


app = Flask(__name__)
app.secret_key = 'keep_me_sane'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/health")
def healthcheck():
    return render_template('health.html')


@app.route("/prediction", methods=['POST'])
def prediction():

    date_obj = request.form['date']
    item_id = request.form['item_id']
    store_id = request.form['store_id']

    sales_prediction(date_obj, item_id, store_id)

    return redirect(url_for('get_sales_prediction'))


@app.route("/sales/stores/items")
def get_sales_prediction():
    y_pred = np.load('data/y_pred.npy')
    return render_template('prediction.html', y_pred=y_pred)


@app.route("/sales/national/", methods=['GET', 'POST'])
def forecast():
    input_date = request.form['input_date']

    import statsmodels.api as sm
    import pandas as pd

    data_df = pd.read_csv('data/df_forecast.csv')
    data_df = data_df.set_index('date_2')

    data = data_df.loc['2011-02-06': input_date]

    # Fit an ARIMA model (you may need to tune hyperparameters)
    model = sm.tsa.ARIMA(data, order=(2, 1, 1))
    results = model.fit()

    # Make forecasts for the next 7 days starting from the specified date
    forecast_vol = results.get_forecast(steps=7).predicted_mean

    return render_template('forecast.html', forecast_vol=forecast_vol)


