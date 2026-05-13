CREATE OR REPLACE VIEW stg_service_requests AS

SELECT
    unique_key,
    created_date,
    agency,
    complaint_type,
    borough,
    status,
    created_hour,
    created_dayofweek

FROM raw_service_requests;