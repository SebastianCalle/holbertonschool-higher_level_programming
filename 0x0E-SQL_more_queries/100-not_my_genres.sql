-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN
	(SELECT tv_genres.name
	FROM tv_shows
  INNER JOIN tv_show_genres
	ON tv_shows.title = 'Dexter' AND tv_show_genres.show_id = tv_shows.id
	INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id)
ORDER BY tv_genres.name ASC;
