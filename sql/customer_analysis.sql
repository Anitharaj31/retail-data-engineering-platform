USE retail_db;

-- Top 10 Customers

SELECT
    customer_id,
    COUNT(transaction_id) AS total_orders,
    SUM(amount) AS total_spent
FROM sales_transactions
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
