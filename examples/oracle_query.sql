SELECT
    NVL(customer_name, 'UNKNOWN') AS customer_name,
    SYSDATE AS extracted_at
FROM customers
WHERE ROWNUM <= 100
START WITH parent_id IS NULL
CONNECT BY PRIOR customer_id = parent_id;
