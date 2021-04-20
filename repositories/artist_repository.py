from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    result = run_sql(sql, values)
    id = result[0]['id']
    artist.id = id
    return artist 
# inserts artist object into artists table in database and retrieves the new serial ID via the returning statement



def select(id):
    result = None
    sql = "SELECT * FROM artists WHERE id = (%s)"
    values = [id] 
    result = run_sql(sql, values)[0]
# result of search is raw data that comes back from database 
    if result is not None:
        artist = Artist(result.name)
    return artist

def select_albums(artist):
    selected_albums = []
    sql = "SELECT * FROM albums WHERE artist_id = (%s)"
    values = [id]
    albums_found = run_sql(sql, values) 
# albums found is raw data that comes back from database
    for row in albums_found:
        artist = Artist(row['name'])
        album = Album(row['title'], row['genre'], artist)
        selected_albums.append(album)
    
    return selected_albums

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)
