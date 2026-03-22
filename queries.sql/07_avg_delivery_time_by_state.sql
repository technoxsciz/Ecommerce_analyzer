-- What is the average delivery time in days for each state, ordered from fastest to slowest?

SELECT`
    round(
        avg(
            EXTRACT(DAY FROM (order_delivered_timestamp::timestamp - order_purchase_timestamp::timestamp))
        ):: numeric, 2
    ) as average_delivery_time_days,
    cust.customer_state

FROM orders as ord

LEFT JOIN customers as cust
    ON ord.customer_id = cust.customer_id

WHERE ord.order_delivered_timestamp IS NOT NULL
AND ord.order_purchase_timestamp IS NOT NULL

GROUP BY
    cust.customer_state
ORDER BY
    average_delivery_time_days ASC;
