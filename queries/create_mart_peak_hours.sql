CREATE OR REPLACE TABLE mart_peak_hours AS

SELECT
    created_hour,
    COUNT(*) AS total_complaints

FROM stg_service_requests

GROUP BY created_hour

ORDER BY total_complaints DESC;