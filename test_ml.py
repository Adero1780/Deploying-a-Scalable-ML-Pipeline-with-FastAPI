import pytest
import numpy as np

from ml.model import train_model, inference, compute_model_metrics

# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_train_model_returns_fitted_estimator():
    """
    # add description for the first test
    """
    # Your code here
    """
    Ensure train_model returns a fitted estimator with a predict method.
    """
    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])
    model = train_model(X, y)
    assert hasattr(model, "predict")


# TODO: implement the second test. Change the function name and input as needed
def test_inference_output_shape():
    """
    # add description for the second test
    """
    # Your code here
    """
    Ensure inference returns predictions of the correct shape.
    """
    X = np.array([[0, 1], [1, 0]])
    y = np.array([0, 1])
    model = train_model(X, y)
    preds = inference(model, X)
    assert preds.shape[0] == X.shape[0]


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_values():
    """
    # add description for the third test
    """
    # Your code here
    """
    Ensure compute_model_metrics returns values between 0 and 1.
    """
    y_true = np.array([0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
