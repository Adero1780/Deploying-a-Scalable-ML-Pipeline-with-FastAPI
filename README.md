# ML Pipeline API with FastAPI
    
## Overview

This project deploys a machine learning model using FastAPI. The model predicts whether an individual's income is <=50K or >50K based on census‑like features (age, education, occupation, hours worked, etc.).

The API exposes two endpoints:
* GET / → Returns a welcome message to confirm the server is running.

* POST /predict → Accepts a JSON payload of features, processes the input using the trained encoder and model, and returns the prediction as a string label.

## Environment Setup
Working in a command-line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or WSL2 is recommended.
* Option 1: use the supplied file environment.yml to create a new environment with conda
* Option 2: use the supplied file requirements.txt to create a new environment with pip

## Repositories
* Create a directory for the project and initialize git.
* As you work on the code, continually commit changes. Trained models you want to use in production must be committed to GitHub.
* Connect your local git repo to GitHub.
* Setup GitHub Actions on your repo. At minimum, configure it to run pytest and flake8 on push and require both to pass without error.
* Ensure the GitHub Action uses the same Python version as development.

## Data
* Download census.csv and commit it to dvc.
* This data is messy; try to open it in pandas and inspect.
* To clean it, use a text editor to remove all spaces.

## Model
* Using the starter code, train a machine learning model on the clean data and save the model.
* Complete any unfinished functions in the starter code.
* Write unit tests for at least 3 functions in the model code.
* Write a function that outputs the performance of the model on slices of the data (suggestion: categorical features).
* Write a model card using the provided template.

## API Creation
* Create a RESTful API using FastAPI with:
* GET / → returns a welcome message.
* POST /predict → performs model inference.

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
* Swagger UI screenshots and client outputs are embedded in the Word Document.
* The API is reproducible: same inputs yield the same outputs.
