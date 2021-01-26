from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/predict', methods = ['GET', 'POST'])
def result():
    if request.method == "POST":

        class_coach = {'first class': 1, 'second class': 2, 'third class': 3}
        sex = {'male': 0, 'female': 1}
        passenger_dict = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 'above 8': 9}
        survival = {0: 'Has Not Survived', 1: 'Has Survived'}

        coach_number = class_coach[request.form['coach_number']]
        gender = sex[request.form['gender_class']]
        age = float(request.form['age'])
        fare = ((float(request.form['fare'])+0.5)**0.07730750998381697 - 1)/0.07730750998381697
        passengers = request.form['passengers']

        passenger_count = [0, 0, 0, 0, 0, 0, 0, 0]

        if int(passengers) > 8:
            passengers = 'above 8'

        passengers = passenger_dict[passengers]
        if passengers == 1:
            p2, p3, p4, p5, p6, p7, p8, p9 = passenger_count
        else:
            passenger_count[passengers-2] = 1
            p2, p3, p4, p5, p6, p7, p8, p9 = passenger_count

        model = pickle.load(open('final_model_v4.pkl', 'rb'))
        scale = pickle.load(open('scaler.pkl', 'rb'))
        pca = pickle.load(open('principal_component.pkl', 'rb'))

        predicted = model.predict(pca.transform(scale.transform([[coach_number, gender, age, fare, p2, p3, p4, p5, p6,
                                                                  p7, p8, p9]])))[0]

        print(predicted)
        return render_template("result.html", prediction=survival[predicted])


if __name__ == '__main__':
    app.run(debug=True)