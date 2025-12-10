CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY, 
    userId INTEGER,
    title TEXT,
    body TEXT
);

CREATE TABLE IF NOT EXISTS comentarios (
    id INTEGER PRIMARY KEY, 
    postId INTEGER,
    name TEXT,
    email TEXT,
    body TEXT,
    FOREIGN KEY(postId) REFERENCES posts(id)
);