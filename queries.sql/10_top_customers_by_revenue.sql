-- Who are the top 10 customers by total amount spent, showing their city and state?

SELECT 
    customers.customer_id,
    customers.customer_city,
    customers.customer_state,
    round(sum(oi.price):: numeric,2) as total_spent

 FROM customers

LEFT JOIN orders as ord
ON customers.customer_id = ord.customer_id

LEFT JOIN order_items as oi
on oi.order_id = ord.order_id

GROUP BY
    customers.customer_id,customers.customer_city,customers.customer_state

ORDER BY
    total_spent DESC

LIMIT 10
