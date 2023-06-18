import pickle
from flask import Flask, request, jsonify, Blueprint, render_template
import jwt
import time

model = None
with open('model/model.pkl','rb') as pickle_file:
   model = pickle.load(pickle_file)
   
   
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # POST 요청에서 form 데이터 받기
    data = request.form
    # 요청이 비어있는지 확인
    if not data:
        return render_template('predict.html', WAR=None)
    
    headers = [
        'k_per_9', 'bb_per_9', 'ops', 'whip', 'fastball_velocity', 'slider_velocity',
        'curve_velocity', 'changeup_velocity', 'splitter_velocity', 'sinker_velocity',
        'knuckle_velocity', 'other_velocity', 'fastball_percentage', 'slider_percentage',
        'curve_percentage', 'changeup_percentage', 'splitter_percentage', 'sinker_percentage',
        'knuckle_percentage', 'other_percentage', 'zone_percentage'
    ]

    # 데이터 전처리
    input_data = [float(data.get(column, 0)) if data.get(column, '') != '' else 0 for column in headers]

    # WAR 값 예측
    war_pred = model.predict([input_data])[0]

    # 결과 반환
    return render_template('predict.html', WAR=war_pred)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run(debug=True)
