import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("NIN")
artist_repository.save(artist_1)

artist_2 = Artist("David Bowie")
artist_repository.save(artist_2)

album_1 = Album("Pretty Hate Machine", "Industrial Pop-Rock",)
album_repository.save(album_1)
album_2 = Album("Broken", "Alt-Metal")
album_repository.save(album_2)
album_3 = Album("Hunky Dory", "Rock")
album_repository.save(album_3)
album_4 = Album("The Next Day", "Rock")
album_repository.save(album_4)


pdb.set_trace()
