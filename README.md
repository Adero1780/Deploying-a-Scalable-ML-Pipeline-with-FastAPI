# ML Pipeline API with FastAPI
    
## Overview

This project deploys a machine learning model using FastAPI. The model predicts whether an individual's income is <=50K or >50K based on census‑like features (age, education, occupation, hours worked, etc.).

The API exposes two endpoints:
* GET / → Returns a welcome message to confirm the server is running.

* POST /predict → Accepts a JSON payload of features, processes the input using the trained encoder and model, and returns the prediction as a string label.

### Quick Start

Clone the repository:
git clone https://github.com/adero1780/Deploying-a-Scalable-ML-Pipeline-with-FastAPI.git
cd Deploying-a-Scalable-ML-Pipeline-with-FastAPI

## Environment Setup
Working in a command-line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or WSL2 is recommended.
* Option 1: use the supplied file environment.yml to create a new environment with conda
* Option 2: use the supplied file requirements.txt to create a new environment with pip

## Repositories & CI
* Create a directory for the project and initialize git.
* As you work on the code, continually commit changes. Trained models you want to use in production must be committed to GitHub.
* Connect your local git repo to GitHub.
* Setup GitHub Actions in .github/workflows/ci.yml.
    * Configured to run pytest and flake8 on push.
    * Both must pass without error.
* Ensure the GitHub Action uses the same Python version as development.
* Evidence: See screenshots/continuous_integration.png.

## Data
* Download census.csv and commit it to dvc.
* This data is messy; try to open it in pandas and inspect.
* To clean it, use a text editor to remove all spaces and process with scikit-learn encoders.

## Model
* Trained using scikit‑learn’s RandomForestClassifier.
* Functions implemented in ml/model.py: training, saving/loading, inference, metrics, and slice performance.
* Artifacts saved in model/ (model.pkl, encoder.pkl, lb.pkl).
* Slice metrics written to slice_output.txt.
* Evidence: See model_card.md for details and metrics.

##Unit Tests
* At least 3 unit tests implemented in tests/test_ml.py.
* Run locally with pytest.
* Evidence: See screenshots/unit_test.png.

## API Creation
* FastAPI app (main.py) with:
* GET / → returns a welcome message.
* POST /predict → performs model inference.
* Client script (local_api.py) demonstrates both outcomes (<=50K and >50K).

* ### Evidence:
    * screenshots/local_api.png → terminal outputs.
    * screenshots/swagger_get.png → Swagger GET.
    * screenshots/swagger_post_data1.png → Swagger POST (<=50K).
    * screenshots/swagger_post_data2.png → Swagger POST (>50K).

## Running the API
* Start the server:
    * uvicorn main:app --reload

* Run the client script:
    * python local_api.py
* This demonstrates both outcomes (<=50K and >50K).

## Demonstration
Screenshots of Swagger UI (GET and POST requests) and terminal outputs are included in ML_Pipeline_API_Submission.docx.

## Versions Used
* Python 3.10
* FastAPI 0.95+
* Uvicorn 0.22+
* scikit-learn

## Notes for Reviewers
* Both inference paths (<=50K and >50K) are demonstrated.
* All screenshots are located in the screenshots/ folder.
* Slice metrics are in slice_output.txt.
* Model details and metrics are documented in model_card.md.
* The API is reproducible: same inputs yield the same outputs.
