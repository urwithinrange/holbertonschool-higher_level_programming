-- list all the cities of CA found in DB usa
SELECT id, name FROM states WHERE name = 'California' ORDER BY cities.id ASC;