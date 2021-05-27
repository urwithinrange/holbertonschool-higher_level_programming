-- highest city temp top 3
SELECT city,AVG(value) AS avg_temp FROM temperatures GROUP BY state ORDER BY avg_temp ASC LIMIT 3;