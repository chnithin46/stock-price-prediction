-- Data Preprocessing SQL for Stock Price Prediction
CREATE TABLE StockPrices (
    Date DATE PRIMARY KEY,
    Open DECIMAL(10,2),
    High DECIMAL(10,2),
    Low DECIMAL(10,2),
    Close DECIMAL(10,2),
    Volume INT
);

-- Insert sample data
INSERT INTO StockPrices (Date, Open, High, Low, Close, Volume)
VALUES
('2023-01-01', 150.5, 250.0, 80.5, 200.8, 5000),
('2023-01-02', 160.2, 260.5, 85.3, 210.5, 5500),
('2023-01-03', 140.7, 245.3, 78.9, 195.4, 4800),
('2023-01-04', 170.1, 270.8, 90.0, 220.6, 6000),
('2023-01-05', 155.9, 265.2, 88.2, 215.3, 5800);

-- Check for missing values
SELECT * FROM StockPrices WHERE Close IS NULL;
