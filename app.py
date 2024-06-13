import numpy as np
from flask import Flask, request,  render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open('diplom_pipeline.pkl', 'rb'))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    # Pipeline
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "Стоимость недвижимости {}".format(*prediction))

if __name__ == "__main__":
    flask_app.run('localhost', 5000)#debug=True)
