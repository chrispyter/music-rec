CREATE DATABASE music_rec;
USE music_rec;

CREATE TABLE songs
(song_name VARCHAR(75) NOT NULL,
artist VARCHAR(75) NOT NULL,
song_id INT PRIMARY KEY AUTO_INCREMENT);

CREATE TABLE tags
(tag VARCHAR(75) NOT NULL,
tag_id INT PRIMARY KEY AUTO_INCREMENT);

CREATE TABLE song_tags
(song_id INT,
tag_id INT,
FOREIGN KEY (song_id) REFERENCES songs(song_id),
FOREIGN KEY (tag_id) REFERENCES tags(tag_id),
PRIMARY KEY (song_id, tag_id));