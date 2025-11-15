# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Model type: RandomForestClassifier (scikit‑learn)

Version: 1.0

Framework: scikit‑learn 1.x

Artifacts: model.pkl, encoder.pkl, lb.pkl

Owner: Domany (ML DevOps course project)

## Intended Use

Primary purpose: Predict whether an individual’s income is <=50K or >50K based on census features.

Intended users: Course reviewers and instructors validating ML DevOps pipeline functionality.

Out of scope: Production deployment, financial or hiring decisions.

## Training Data

Dataset: U.S. Census Income dataset (census.csv).

Features: Age, workclass, education, marital status, occupation, race, sex, hours per week, native country, etc.

Label: salary (<=50K or >50K).

Split: 80% training, 20% testing.

## Evaluation Data

Held‑out test set: 20% of census data.

Slice metrics: Evaluated across categorical slices to check fairness and performance consistency.

File: Results saved in slice_output.txt.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

Overall performance (test set):

Precision: 0.7419

Recall: 0.6384

F1 score: 0.6863

## Ethical Considerations

Bias: Census data may reflect historical and societal biases. Predictions could inherit these biases.

Fairness: Slice metrics highlight disparities across groups.

Responsible use: Not suitable for real‑world decision‑making without fairness audits.

## Caveats and Recommendations

Limitations: Model trained on a single dataset; may not generalize.

Recommendations:

Extend with fairness checks and bias mitigation for production.

Document preprocessing steps for reproducibility.
