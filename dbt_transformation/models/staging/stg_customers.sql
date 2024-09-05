# dbt_transformation/models/staging/stg_customers.sql

select customer_id, email, gender, city, country
from {{ source("RawDataset", "customers") }}