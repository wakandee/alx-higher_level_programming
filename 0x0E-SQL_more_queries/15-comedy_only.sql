-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)

-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT title FROM tv_genres RIGHT JOIN tv_show_genres tsg ON tv_genres.id=tsg.genre_id 
RIGHT JOIN tv_shows ON tsg.show_id = tv_shows.id WHERE name = 'Comedy' GROUP BY tv_shows.id ORDER BY title ASC;