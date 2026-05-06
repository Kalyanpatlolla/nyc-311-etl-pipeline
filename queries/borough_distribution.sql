SELECT 
    borough,
    COUNT(*) AS total_requests
FROM `nyc-etl-project.nyc_311_pipeline.service_requests`
GROUP BY borough
ORDER BY total_requests DESC;