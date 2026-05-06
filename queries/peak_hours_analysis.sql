SELECT 
    created_hour,
    COUNT(*) AS total_requests
FROM `nyc-etl-project.nyc_311_pipeline.service_requests`
GROUP BY created_hour
ORDER BY total_requests DESC;