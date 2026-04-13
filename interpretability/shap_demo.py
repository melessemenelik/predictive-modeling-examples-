# interpretability/shap_demo.py
import shap
import xgboost
import pandas as pd

# Synthetic dataset
X = pd.DataFrame({
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [10, 20, 30, 40, 50]
})
y = [0, 1, 0, 1, 0]

model = xgboost.XGBClassifier()
model.fit(X, y)

explainer = shap.Explainer(model, X)
shap_values = explainer(X)

shap.summary_plot(shap_values, X)
