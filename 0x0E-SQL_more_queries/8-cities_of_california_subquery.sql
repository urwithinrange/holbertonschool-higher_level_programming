-- list all the cities of CA found in DB usa
SELECT id, name FROM cities WHERE state_id = 1 GROUP BY id ASC;