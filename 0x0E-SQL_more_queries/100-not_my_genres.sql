-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)

-- Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (
    SELECT tg.id
    FROM tv_genres tg
    INNER JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
    INNER JOIN tv_shows ts ON tsg.show_id = ts.id
    WHERE ts.title = 'Dexter'
)
ORDER BY tg.name ASC;


