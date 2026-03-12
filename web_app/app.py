from flask import Flask, render_template, request, jsonify
import pickle

# Flask app create
app = Flask(__name__)

# Load ML model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    sender = data["sender"]
    subject = data["subject"]
    message = data["message"]

    text = sender + " " + subject + " " + message

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)

    if prediction[0] == 1:
        result = "spam"
    else:
        result = "ham"

    return jsonify({"result": result})


# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)