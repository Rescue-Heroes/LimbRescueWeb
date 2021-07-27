from pathlib import Path

from limbresml.utils import load_model, preprocess_single_file


def predict(file):
    X, _ = preprocess_single_file(file, label=None, n_samples="center")
    model = Path("SVM.joblib")
    model = load_model(model.absolute())
    pred = model.predict(X)[0]
    return pred
