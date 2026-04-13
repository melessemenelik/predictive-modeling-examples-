# regression/housing_prices.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Synthetic dataset
data = pd.DataFrame({
    "sqft": [800, 1000, 1200, 1500, 1800],
    "price": [150000, 180000, 200000, 250000, 300000]
})

X = data[["sqft"]]
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("Predictions:", preds)
print("RMSE:", mean_squared_error(y_test, preds, squared=False))
