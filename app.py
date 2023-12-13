from flask import Flask, render_template, request
import joblib 

app = Flask(__name__)

mpg_model = joblib.load("models\mpg_model.joblib")
diabetes_model = joblib.load("models\diabetes_model.joblib")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mpg', methods=['GET', 'POST'])
def predict_mpg():
    if request.method == 'POST':
        cylinders = request.form.get('cylinders', type=int)
        displacement = request.form.get('displacement', type=float)
        horsepower = request.form.get('horsepower', type=float)
        weight = request.form.get('weight', type=float)
        acceleration = request.form.get('acceleration', type=float)
        model_year = request.form.get('model_year', type=int)
        origin = request.form.get('origin')

        prediction = mpg_model.predict([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin_numeric]])

        return render_template('prediction_result.html', result=prediction)

    return render_template('mpg_form.html')


@app.route('/diabetes', methods=['GET', 'POST'])
def predict_diabetes():
    if request.method == 'POST':
        pregnancies = request.form.get('pregnancies', type=int)
        glucose = request.form.get('glucose', type=float)
        bloodPressure = request.form.get('bloodPressure', type=float)
        skinThickness = request.form.get('skinThickness', type=float)
        insulin = request.form.get('insulin', type=float)
        bmi = request.form.get('bmi', type=float)
        diabetesPedigreeFunction = request.form.get('diabetesPedigreeFunction', type=float)
        age = request.form.get('age', type=int)

        prediction = diabetes_model.predict([[pregnancies, glucose, bloodPressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]])

        return render_template('prediction_result.html', result=prediction)

    return render_template('diabetes_form.html')


if __name__ == '__main__':
    app.run(debug=True)
