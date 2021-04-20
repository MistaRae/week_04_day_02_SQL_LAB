from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    album = None
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.genre, album.artist_id]
    result = run_sql(sql, values)
    id = result[0]['id']
    album.id = id
    return album
    # inserts album object into albums table in database and retrieves the new serial ID via the returning statement


def select(id):
    result = None
    sql = "SELECT * FROM albums WHERE id = (%s)"
    values = [id]
    result = run_sql(sql, values)
# returns raw data corresponding to the ID (provided as argument) found on the albums table.

# reconstructing data as album object, if found:
    if result is not None:
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
    return album


def delete(id):
    sql = "DELETE * FROM albums WHERE id = (%s)"
    values = [id]
    run_sql(sql,values)
    
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

    