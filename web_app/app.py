from flask import Flask, render_template, request, jsonify
import pickle
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))



# Flask app create


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
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)