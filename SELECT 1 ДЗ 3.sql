-- Название и продолжительность самого длительного трека.
	SELECT name, duration 
	  FROM song
  ORDER BY duration DESC LIMIT 1;
  
-- Название треков, продолжительность которых не менее 3,5 минут.
  	SELECT name
  	  FROM song
  	 WHERE duration >= '00:03:30';
  	 
-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
	SELECT name 
	  FROM collection
     WHERE year_of_issue >= 2018 AND year_of_issue <= 2020;
    
-- Исполнители, чьё имя состоит из одного слова.
	SELECT name_alias 
	  FROM executor
     WHERE name_alias NOT LIKE '% %';
     
-- Название треков, которые содержат слово «мой» или «my».
    SELECT name
	  FROM song
     WHERE    name LIKE 'мой' 
     	   OR name LIKE 'my'
     	   OR name LIKE '% мой %' 
     	   OR name LIKE '% my %'
     	   OR name LIKE '% мой' 
     	   OR name LIKE '% my'
     	   OR name LIKE 'мой %' 
     	   OR name LIKE 'my %';