
SELECT country, COUNT(*) AS total_customers
FROM clean_customers
GROUP BY country
ORDER BY total_customers DESC;

SELECT AVG(purchase_amount) AS average_purchase
FROM clean_customers;

SELECT COUNT(*) AS total_records
FROM clean_customers;
