-- highest city temp top 3
SELECT city,AVG(value) AS avg_temp FROM temperatures GROUP BY state city ORDER BY avg_temp DEC LIMIT 3;