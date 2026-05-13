CREATE OR REPLACE TABLE mart_top_complaints AS

SELECT
    complaint_type,
    COUNT(*) AS total_complaints

FROM stg_service_requests

GROUP BY complaint_type

ORDER BY total_complaints DESC;