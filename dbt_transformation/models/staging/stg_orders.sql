# dbt_transformation/models/staging/stg_orders.sql

select
    order_id,
    customer_id,
    status as order_status,
    order_approved_at,
    order_delivered_at,
from {{ source("RawDataset", "orders") }}