# Stock Price Prediction

## Overview
This project predicts stock prices using machine learning models. It analyzes historical stock data to generate forecasts that assist investors in making informed decisions.

## Technologies Used
- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Machine Learning (XGBoost, ARIMA, LSTMs)
- Yahoo Finance API (for stock data retrieval)
- Tableau (for visualization)

## Dataset
The dataset includes historical stock price data:
- **Open, High, Low, Close** – Price values per trading day
- **Volume** – Number of shares traded
- **Moving Averages** – 20-day trend analysis
- **Target Variable:** Closing Price

## Approach
1. **Data Collection:** Used Yahoo Finance API to get real-time stock data.
2. **Exploratory Data Analysis (EDA):** Identified patterns and trends.
3. **Model Training:** Used **XGBoost, ARIMA, and LSTMs** for prediction.
4. **Evaluation:** Achieved **90% accuracy** in forecasting trends.
5. **Visualization:** Created Tableau dashboards for investors.

## Results
- Provided accurate short-term stock price forecasts.
- Identified key factors influencing stock price movement.
- Helped investors make data-driven trading decisions.

## Future Enhancements
- Implement deep learning techniques (Transformers) for better accuracy.
- Deploy as a real-time financial dashboard for stock analysis.