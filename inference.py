import joblib
import numpy as np


def load_model(path="iris_model.joblib"):
    return joblib.load(path)


def predict(model, features: dict) -> str:
    data = np.array(
        [
            [
                features["sepal_length"],
                features["sepal_width"],
                features["petal_length"],
                features["petal_width"],
            ]
        ]
    )
    prediction = model.predict(data)
    class_names = ["setosa", "versicolor", "virginica"]
    return class_names[prediction[0]]
