USE retail_db;

-- Daily Sales Trend

SELECT
    DATE(transaction_time) AS sales_date,
    COUNT(transaction_id) AS transactions,
    SUM(amount) AS daily_revenue
FROM sales_transactions
GROUP BY DATE(transaction_time)
ORDER BY sales_date;
