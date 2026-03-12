# from flask import Flask, render_template, request, jsonify
import pickle
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask app with templates folder
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

# Load ML model and vectorizer
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    sender = data.get("sender", "")
    subject = data.get("subject", "")
    message = data.get("message", "")

    text = sender + " " + subject + " " + message

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)

    result = "spam" if prediction[0] == 1 else "ham"

    return jsonify({"result": result})


# Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=porfrom flask import Flask, render_template, request, jsonify
import pickle
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask app with templates folder
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

# Load ML model and vectorizer
model_path = os.path.join(BASE_DIR, "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    sender = data.get("sender", "")
    subject = data.get("subject", "")
    message = data.get("message", "")

    text = sender + " " + subject + " " + message

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)

    result = "spam" if prediction[0] == 1 else "ham"

    return jsonify({"result": result})


# Run server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
