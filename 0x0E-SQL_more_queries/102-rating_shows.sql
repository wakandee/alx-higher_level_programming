-- 19. Rotten tomatoes
SELECT CONCAT(ts.title, ' - ', IFNULL(SUM(tr.rate), 0)) AS show_rating
FROM tv_shows ts
LEFT JOIN tv_show_ratings tr ON ts.id = tr.show_id
GROUP BY ts.id, ts.title
ORDER BY SUM(tr.rate) DESC;