SELECT 
    borough,
    complaint_type,
    COUNT(*) AS total_complaints
FROM `nyc-etl-project.nyc_311_pipeline.service_requests`
GROUP BY borough, complaint_type
ORDER BY total_complaints DESC
LIMIT 10;