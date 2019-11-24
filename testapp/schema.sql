DROP TABLE IF EXISTS flaskuser;

CREATE TABLE flaskuser (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    pword TEXT NOT NULL
);