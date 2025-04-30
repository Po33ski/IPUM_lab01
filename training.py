from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


def load_data():
    data = load_iris()
    return data.data, data.target, data.target_names


# X - features matrix, y - labels
def train_model():
    X, y, _ = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return model


def save_model(model, filename="iris_model.joblib"):
    joblib.dump(model, filename)


if __name__ == "__main__":
    model = train_model()
    save_model(model)
