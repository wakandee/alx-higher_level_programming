-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)

-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres RIGHT JOIN tv_show_genres tsg ON tv_genres.id=tsg.genre_id 
RIGHT JOIN tv_shows ON tsg.show_id = tv_shows.id WHERE tv_shows.title IS NOT NULL GROUP BY tv_genres.id ORDER BY number_of_shows DESC;