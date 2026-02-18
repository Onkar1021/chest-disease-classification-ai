import os
from unittest import result
from Respire.Utils import decodeImage
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, render_template
from Respire.Pipeline.Prediction_Pipeline import PredictionPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        data = request.get_json()

        if not data or "image" not in data:
            return jsonify({"error": "No image received"}), 400

        image = data["image"]
        decodeImage(image, clApp.filename)

        result = clApp.classifier.predict()
        return jsonify(result)

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host="0.0.0.0", port=5000, debug=True) #for AWS