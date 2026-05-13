CREATE OR REPLACE TABLE mart_complaints_by_borough AS

SELECT
    borough,
    COUNT(*) AS total_complaints

FROM stg_service_requests

GROUP BY borough

ORDER BY total_complaints DESC;