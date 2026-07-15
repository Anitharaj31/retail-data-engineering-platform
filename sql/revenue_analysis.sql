USE retail_db;

-- Revenue by Category

SELECT
    revenue_category,
    COUNT(*) AS total_transactions,
    SUM(amount) AS total_revenue,
    AVG(amount) AS average_transaction_value
FROM sales_transactions
GROUP BY revenue_category
ORDER BY total_revenue DESC;
