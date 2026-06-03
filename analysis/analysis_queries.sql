
-- Total customers by country
SELECT country, COUNT(*) AS total_customers
FROM clean_customers
GROUP BY country
ORDER BY total_customers DESC;

-- Average purchase amount
SELECT AVG(purchase_amount) AS average_purchase
FROM clean_customers;

-- Total cleaned records
SELECT COUNT(*) AS total_records
FROM clean_customers;

-- Highest spending customers
SELECT customer_id, name, email, country, purchase_amount
FROM clean_customers
ORDER BY purchase_amount DESC
LIMIT 10;
