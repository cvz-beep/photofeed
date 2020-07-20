DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE uploaded_pictures (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT foreign key,
  title TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL,
  date
);

