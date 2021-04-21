DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255), 
    artist VARCHAR(255),
    artist_id INT REFERENCES artists(id)
);

-- consider using "ON DELETE CASCADE" after the reference statement on line 14
-- allows you to delete a table entry with dependent keys referenced in other tables

-- is artist required? 