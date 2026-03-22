-- What is the total revenue per month, ordered chronologically?

WITH monthly_revenue as (
SELECT 
    EXTRACT(YEAR from order_purchase_timestamp :: timestamp) as year,
    EXTRACT(MONTH from order_purchase_timestamp :: timestamp) as month,
    order_id
FROM orders
)

select 
    year,
    month,
   round(sum(oi.price):: numeric,2) as total_revenue
from monthly_revenue 

left join order_items as oi
on oi.order_id = monthly_revenue.order_id

group by 
    year,month
order by 
    year asc,month asc; 
