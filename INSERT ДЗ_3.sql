	INSERT INTO genre (name)
	VALUES ('Power metal'),
		   ('Folk'),
		   ('Metal'),
		   ('Heavy metal'),
		   ('Punk');
		  
		  
	INSERT INTO executor (name_alias)
	VALUES ('Powerwolf'),
		   ('Alkonost'),
		   ('Alestorm'),
		   ('Beast in Black'),
		   ('Manntra'),
		   ('Brothers of metal'),
		   ('The Offspring');
		   
	INSERT INTO genre_executor (genre_id, executor_id)
	VALUES (1, 1),
		   (1, 2),
		   (1, 3),
		   (1, 6),
		   (2, 2),
		   (3, 1),
		   (3, 6),
		   (4, 1),
		   (4, 4),
		   (4, 5),
		   (5, 3),
		   (5, 7);
		   
	INSERT INTO album (name, year_of_issue)
	VALUES ('Call of the Wild', 2021),
		   ('Песни белой лилии', 2016),
		   ('No Grave But The Sea', 2017),
		   ('From Hell with Love', 2019),
		   ('Kreatura', 2022),
		   ('Emblas Saga', 2020),
		   ('Conspiracy of One', 2000);
		  
	INSERT INTO executor_album (executor_id, album_id)
	VALUES (1, 1),
		   (2, 2),
		   (3, 3),
		   (4, 4),
		   (5, 5),
		   (6, 6),
		   (7, 7);
		   
	INSERT INTO song (album_id, "name", duration)
	VALUES (1, 'Dancing with the Dead', '00:04:03'),
		   (1, 'Blood for Blood (Faoladh)', '00:03:12'),
		   (2, 'Русалка', '00:03:57'),
		   (2, 'Река', '00:04:54'),
		   (3, 'No Grave But The Sea', '00:03:30'),
		   (4, 'True Believer', '00:03:28'),
		   (4, 'Killed by Death', '00:03:52'),
		   (5, 'Volhov', '00:03:34'),
		   (6, 'Powersnake', '00:03:44'),
		   (7, 'One Fine Day', '00:02:45');
		   
	INSERT INTO collection (name, year_of_issue)
	VALUES ('Best of power metal', 2019),
		   ('Metal head', 2022),
		   ('PUNKOFF', 2020),
		   ('Alternativ', 2023);
		   
	INSERT INTO collection_song (collection_id, song_id)
	VALUES (1, 1),
		   (1, 2),
		   (1, 6),
		   (1, 7),
		   (1, 9),
		   (2, 1),
		   (2, 7),
		   (2, 9),
		   (3, 5),
		   (3, 10),
		   (4, 3),
		   (4, 4),
		   (4, 8);
		  
	INSERT INTO song (album_id, "name", duration)
		 VALUES (2, 'my own', '00:02:10'),
		 		(2, 'my', '00:04:00'),
		 		(3, 'own my', '00:01:15'),
		 		(5, 'oh my god', '00:03:12'),
		 		(1, 'myself', '00:01:59'),
		 		(2, 'by myself', '00:04:02'),
		 		(5, 'by myself by', '00:03:00'),
		 		(6, 'beemy', '00:06:00'),
		 		(6, 'premyne', '00:04:01');