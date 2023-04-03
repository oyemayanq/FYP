from flask import Flask, render_template,request
#import pickle

app = Flask(__name__)
#model = pickle.load(open('model.pkl','rb'))

@app.route("/")
def hello():
    return render_template("index.html")

#@app.route("/predict",methods=['POST'])
#def predict():
#    room = int(request.form['rooms'])
#    distance = int(request.form['distance'])

#    prediction = model.predict([[room,distance]])
#    output = round(prediction[0],2)
#    return render_template("index.html",prediction_text = f'${output}')


if __name__ == "__main__":
    app.run()