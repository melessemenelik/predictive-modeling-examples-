# classification/churn_prediction.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Synthetic dataset
data = pd.DataFrame({
    "age": [25, 45, 35, 50, 23],
    "tenure": [1, 10, 5, 12, 2],
    "churn": [1, 0, 0, 0, 1]
})

X = data[["age", "tenure"]]
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

preds = clf.predict(X_test)
print("Classification Report:\n", classification_report(y_test, preds))
