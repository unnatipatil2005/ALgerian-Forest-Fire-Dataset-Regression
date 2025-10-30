from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

ridge_model=pickle.load(open(r'E:\downloads\Ridge+Lassso+Elastic+Regression+Practicals\Ridge Lassso Elastic Regression Practicals\models\ridge.pkl','rb'))
standard_scaler=pickle.load(open(r'E:\downloads\Ridge+Lassso+Elastic+Regression+Practicals\Ridge Lassso Elastic Regression Practicals\models\scaler.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        # Process input and predict
        temperature = float(request.form.get('Temperature'))
        rh = float(request.form.get('RH'))
        ws = float(request.form.get('WS'))
        rain = float(request.form.get('Rain'))
        ffmc = float(request.form.get('FFMC'))
        dmc = float(request.form.get('DMC'))
        isi = float(request.form.get('ISI'))
        classes = float(request.form.get('Classes'))
        region = float(request.form.get('Region'))

        input_data = np.array([[temperature, rh, ws, rain, ffmc, dmc, isi, classes, region]])
        input_scaled = standard_scaler.transform(input_data)
        result = ridge_model.predict(input_scaled)
        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
