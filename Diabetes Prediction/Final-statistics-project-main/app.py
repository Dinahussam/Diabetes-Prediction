from flask import Flask, redirect, url_for, request, render_template
import pickle
import numpy as np

model = pickle.load(open('Diabetes_classifier.pickle', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/hello')
def home():
    return render_template('hello.html')

@app.route('/up')
def up():
    return render_template('upload.html')



@app.route('/hello', methods=['POST'])
def hello():

    Cholesterol = request.form['a']
    Glucose = request.form['b']
    hdl_chol = request.form['c']
    chol_hdl_ratio = request.form['d']
    age = request.form['e']
    gender = request.form['f']
    hight = request.form['g']
    weight = request.form['h']
    bmi = request.form['i']
    Systolic_bp = request.form['j']
    diastolic_bp = request.form['k']
    waist = request.form['l']
    hip = request.form['m']
    waist_hip_ratio = request.form['n']
    if (gender == "Male"):
        male = 1
    else:
        male = 0

    Cholesterol = int(Cholesterol)
    Glucose = int(Glucose)
    hdl_chol = int(hdl_chol)
    chol_hdl_ratio = float(chol_hdl_ratio)
    age = int(age)
    gender = (gender)
    hight = int(hight)
    weight = int(weight)
    bmi = float(bmi)
    Systolic_bp = int(Systolic_bp)
    diastolic_bp = int(diastolic_bp)
    waist = int(waist)
    hip = int(hip)
    waist_hip_ratio = float(waist_hip_ratio)

    features = np.array([(Cholesterol, Glucose, hdl_chol, chol_hdl_ratio, age, male, hight, weight, bmi, Systolic_bp,
                          diastolic_bp, waist, hip, waist_hip_ratio)])
    prediction = model.predict(features)
    if prediction == 0:
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"
    return render_template('hello.html', prediction_text=' The patient has:{}'.format(prediction))


if __name__ == '__main__':
    app.run(debug=True)
