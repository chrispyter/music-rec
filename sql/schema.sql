CREATE TABLE songs
(song_name VARCHAR(75) NOT NULL,
artist VARCHAR(75) NOT NULL,
song_id INTEGER PRIMARY KEY AUTOINCREMENT,
UNIQUE(song_name, artist));

CREATE TABLE tags
(tag VARCHAR(75) NOT NULL,
tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
UNIQUE(tag));

CREATE TABLE song_tags
(song_id INTEGER,
tag_id INTEGER,
FOREIGN KEY (song_id) REFERENCES songs(song_id),
FOREIGN KEY (tag_id) REFERENCES tags(tag_id),
PRIMARY KEY (song_id, tag_id));