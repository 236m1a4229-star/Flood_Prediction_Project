from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("models/flood_prediction.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

FEATURES = [
    "Temp",
    "Humidity",
    "Cloud Cover",
    "ANNUAL",
    "Jan-Feb",
    "Mar-May",
    "Jun-Sep",
    "Oct-Dec",
    "avgjune",
    "sub"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    values = [float(request.form[feature]) for feature in FEATURES]

    data = pd.DataFrame([values], columns=FEATURES)

    scaled_data = scaler.transform(data)

    prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        result = "⚠️ Flood Likely"
    else:
        result = "✅ No Flood"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)