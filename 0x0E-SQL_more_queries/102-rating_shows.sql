-- script that lists all shows from hbtn_0d_tvshows_rate
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- You can use only one SELECT statement

SELECT title, SUM(rating) AS rating_sum
FROM hbtn_0d_tvshows_rate.shows
GROUP BY title
ORDER BY rating_sum DESC;
