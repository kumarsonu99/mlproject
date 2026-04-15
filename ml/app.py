from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ ADD THIS
import pickle

app = Flask(__name__)
CORS(app)   # ✅ ADD THIS (important)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    text = request.json["text"]
    vec = vectorizer.transform([text])
    result = model.predict(vec)[0]

    return jsonify({
        "result": "Toxic" if result == 1 else "Not Toxic"
    })

if __name__ == "__main__":
    app.run(debug=True)