-- How many orders were paid with each payment type, ordered from most to least?

SELECT 
    payment_type,
    count(*) as total_payments
from payments

GROUP BY
    payment_type
ORDER BY
    total_payments DESC;
