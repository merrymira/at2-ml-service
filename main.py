import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, sessions
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
    date = request.form['date']
    item_id = request.form['item_id']
    store_id = request.form['store_id']

    # Call the sales prediction function with the form data
    sales_prediction(date, item_id, store_id)

    # Redirect to the desired route where you want to display the prediction
    return redirect(url_for('get_sales_prediction'))


@app.route("/forecast", methods=['POST'])
def forecast():
    input_date = request.form['input_date']

    # Call the sales forecast function with the form data
    forecast_nation(input_date)

    # Redirect to the desired route where you want to display the prediction
    return redirect(url_for('get_sales_forecast'))


@app.route("/sales/national", methods=['GET'])
def get_sales_forecast():
    forecast_vol = np.load('data/forecast_values.npy')

    return render_template('forecast.html', forecast_vol=forecast_vol)


@app.route("/sales/stores/items", methods=['GET'])
def get_sales_prediction():
    y_pred = np.load('data/y_pred.npy')
    return render_template('prediction.html', y_pred=y_pred)
