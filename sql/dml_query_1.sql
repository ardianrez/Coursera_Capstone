select order_id, b.customer_id, customer_city,order_purchase_timestamp
from tb_order a left join tb_customer b ON a.customer_id = b.customer_id
where order_status NOT LIKE '%canceled%'