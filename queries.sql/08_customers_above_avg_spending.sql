-- How many orders have a payment value above the overall average payment value?

SELECT 

    count(*) as payment_value_above_average

from payments 

WHERE
    payment_value > (SELECT avg(payment_value) FROM payments)

    
