-- list all records of the second_table that have a 'name'
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;