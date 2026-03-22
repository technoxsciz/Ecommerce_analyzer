-- Which are the top 10 cities with the most customers?

SELECT 
    customer_city,
    count(*) as total_customers
from customers

GROUP BY
    customer_city
ORDER BY
    total_customers DESC

limit 10