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

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def select(id):
    sql = "SELECT * FROM albums WHERE id = (%s)"
    values = [id]
    run_sql(sql, values)
    pass


def delete(id):
    sql = "DELETE * FROM albums WHERE id = (%s)"
    values = [id]
    run_sql(sql,values)
    