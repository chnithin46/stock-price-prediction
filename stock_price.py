import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import yfinance as yf

# Load stock data (Example: Tesla stock data)
stk = yf.Ticker("TSLA")
data = stk.history(period="5y")

# Feature engineering
data["Moving_Avg"] = data["Close"].rolling(window=20).mean()
data.dropna(inplace=True)

# Prepare dataset
X = data[["Open", "High", "Low", "Volume", "Moving_Avg"]]
y = data["Close"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("MSE:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Plot actual vs predicted
plt.figure(figsize=(10,5))
plt.plot(y_test.values, label="Actual Prices")
plt.plot(y_pred, label="Predicted Prices", linestyle="dashed")
plt.legend()
plt.title("Stock Price Prediction")
plt.show()