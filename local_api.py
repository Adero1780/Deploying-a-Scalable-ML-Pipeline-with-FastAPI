import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1:8000/") # Your code here
print(f"GET -> {r.status_code} | {r.json()['message']}")

# TODO: print the status code
# print()
# TODO: print the welcome message
# print()

#Sample payload 1 (<=50K)

data1 = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

r = requests.post("http://127.0.0.1:8000/predict", json=data1)
print(f"POST (data1) → {r.status_code} | Prediction: {r.json()['result']}")

# Sample payload 2 (>50K)
data2 = {
    "age": 45,
    "workclass": "Private",
    "fnlgt": 120000,
    "education": "Doctorate",
    "education-num": 16,
    "marital-status": "Married-civ-spouse",
    "occupation": "Exec-managerial",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 50000,
    "capital-loss": 0,
    "hours-per-week": 60,
    "native-country": "United-States",
}

r = requests.post("http://127.0.0.1:8000/predict", json=data2)
print(f"POST (data2) → {r.status_code} | Prediction: {r.json()['result']}")

# TODO: send a POST using the data above

# TODO: print the status code
# print()
# TODO: print the result
# print()

