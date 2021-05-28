-- list all genre from database and how many shows are linked to each
SELECT tv_genres.name AS genre, COUNT(genre_id) AS number_of_shows FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.show_id
GROUP BY genre ORDER BY number_of_shows DESC;