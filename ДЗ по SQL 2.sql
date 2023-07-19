CREATE TABLE IF NOT EXISTS Genre
(
	Genre_id SERIAL PRIMARY KEY,
	Name CHARACTER VARYING (30) UNIQUE 
);



CREATE TABLE IF NOT EXISTS Executor
(
	Executor_id SERIAL PRIMARY KEY,
	Name_alias CHARACTER VARYING (30) UNIQUE 
);


CREATE TABLE IF NOT EXISTS Genre_Executor
(
	Genre_id INTEGER REFERENCES Genre(Genre_id),
	Executor_id INTEGER REFERENCES Executor(Executor_id),
 	CONSTRAINT one PRIMARY KEY (Genre_id, Executor_id)
 );
 

 CREATE TABLE IF NOT EXISTS Album
 (
 	Album_id SERIAL PRIMARY KEY,
 	Name CHARACTER VARYING (20) UNIQUE,
 	Year_of_issue INTEGER CHECK (Year_of_issue < 9999)
 );
 
 
 CREATE TABLE IF NOT EXISTS Executor_Album
 (
 	Executor_id INTEGER REFERENCES Executor(Executor_id),	
 	Album_id INTEGER REFERENCES Album(Album_id),
 	CONSTRAINT two PRIMARY KEY (Executor_id, Album_id)
 );
 
 
 CREATE TABLE IF NOT EXISTS Song
 (
 	Song_id SERIAL PRIMARY KEY,
 	ALbum_id INTEGER REFERENCES Album(Album_id),
 	Name CHARACTER VARYING (90) UNIQUE,
 	Duration TIME
 );


 CREATE TABLE IF NOT EXISTS Collection
 (
	Collection_id SERIAL PRIMARY KEY,
	Name CHARACTER VARYING (30) UNIQUE,
 	Year_of_issue INTEGER CHECK (Year_of_issue < 9999)
 )

 CREATE TABLE IF NOT EXISTS Collection_Song
 (
	CS_id SERIAL PRIMARY KEY,
	Collection_id INTEGER REFERENCES Collection(Collection_id),
	Song_id INTEGER	REFERENCES Song(Song_id)
 )
