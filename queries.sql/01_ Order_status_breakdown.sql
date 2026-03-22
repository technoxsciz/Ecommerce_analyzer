-- How many orders are there for each status: delivered, cancelled, shipped etc. — ordered from most to least?

SELECT 
    order_status, 
    count(*) as total_orders

FROM orders

GROUP BY
    order_status

ORDER BY
    total_orders DESC;
