-- What is the average payment value for each payment type, rounded to 2 decimal places, ordered from highest to lowest?
SELECT 
    payment_type,
       round(avg(payment_value)::numeric, 2) as average_payment
FROM payments

GROUP BY
    payment_type
ORDER BY
    average_payment DESC;