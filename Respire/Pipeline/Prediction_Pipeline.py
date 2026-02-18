import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:

    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        print("Dummy model prediction running...")

        import random

        classes = ['Normal', 'Adenocarcinoma Cancer']
        prediction = random.choice(classes)
        confidence = round(random.uniform(85, 99), 2)

        if prediction == "Normal":
            explanation = "No visible signs of lung cancer detected. Lungs appear healthy."
        else:
            explanation = "Abnormal tissue growth detected in lung region. Further medical evaluation recommended."

        return {
            "prediction": prediction,
            "confidence": f"{confidence}%",
            "explanation": explanation
        }




