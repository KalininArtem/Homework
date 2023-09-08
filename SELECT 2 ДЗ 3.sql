--Количество исполнителей в каждом жанре.
	SELECT genre_id, count (executor_id) AS Количество_исполнителей
	  FROM genre_executor
  GROUP BY genre_id 
  ORDER BY genre_id ;
	
--Количество треков, вошедших в альбомы 2019–2020 годов.
 	SELECT COUNT(*)
 	  FROM song
 	  JOIN album ON song.album_id = album.album_id 
 	 WHERE album.year_of_issue >= 2019  AND  album.year_of_issue <= 2020;
 	 
--Средняя продолжительность треков по каждому альбому.
	SELECT song.album_id , album.name, AVG (duration) 
	  FROM song 
	  JOIN album ON album.album_id = song.album_id
  GROUP BY song.album_id,album.name
  ORDER BY song.album_id;
  
 --Все исполнители, которые не выпустили альбомы в 2020 году.
  	SELECT name_alias
 	  FROM executor
 	 WHERE name_alias NOT IN (
 	 	   SELECT name_alias
 	 	   	 FROM executor e
 	 	   	 JOIN executor_album AS ea ON ea.executor_id = e.executor_id 
 	  		 JOIN album AS a ON a.album_id = ea.album_id 
 	 		 WHERE a.year_of_issue = 2020);
 	 
--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
	SELECT DISTINCT  c."name" 
	  FROM collection c
	  JOIN collection_song cs ON c.collection_id = cs.collection_id 
	  JOIN song s ON s.song_id = cs.song_id 
	  JOIN album a ON s.album_id = a.album_id 
	  JOIN executor_album ea ON ea.album_id = a.album_id 
	  JOIN executor e ON e.executor_id = ea.executor_id 
	 WHERE e.name_alias LIKE 'Powerwolf';