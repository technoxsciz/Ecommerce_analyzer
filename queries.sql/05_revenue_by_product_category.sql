-- What is the total revenue for each product category, ordered from highest to lowest?

SELECT 
    pd.product_category_name,
    sum(oi.price) as total_revenue

FROM products as pd

LEFT JOIN order_items as oi
on oi.product_id = pd.product_id 

GROUP BY
    pd.product_category_name  

ORDER BY
    total_revenue DESC
