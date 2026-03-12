# from flask import Flask, render_template, request, jsonify
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

# Load model
with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=porfrom flask import Flask, render_template, request, jsonify
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

# Load model
with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
