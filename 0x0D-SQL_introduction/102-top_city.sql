-- highest city temp top 3
SELECT city,AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;