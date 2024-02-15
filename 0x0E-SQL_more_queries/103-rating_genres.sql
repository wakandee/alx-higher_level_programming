-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.

-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tg.name, IFNULL(SUM(tr.rate), 0) AS genre_rating
FROM tv_genres tg
LEFT JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
LEFT JOIN tv_show_ratings tr ON tsg.show_id = tr.show_id
GROUP BY tg.id, tg.name
ORDER BY SUM(tr.rate) DESC;