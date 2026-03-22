-- What are the top 10 product categories by number of orders, ordered from most to least?

SELECT 
    pd.product_category_name,
    count(*) as total_orders
FROM products as pd

INNER JOIN order_items as oi
on oi.product_id = pd.product_id

GROUP BY
    pd.product_category_name
ORDER BY
    total_orders DESC
limit 10 
