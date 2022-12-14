from VinylsBooksVideoGames.models import Vinyls
Vinyls(title="Post", artist="Björk", tracks=11).save()
Vinyls(title="Punisher", artist="Phoebe Bridgers", tracks=11).save()
Vinyls(title="Softie", artist="Wy", tracks=11).save()

from VinylsBooksVideoGames.models import Books
Books(title="Las malas", author="Camila Sosa Villada", year_published=2019).save()
Books(title="Syntactic Structures", author="Noam Chomsky", year_published=1957).save()
Books(title="New World Sourdough", author="Bryan Ford", year_published=2020).save()

from VinylsBooksVideoGames.models import Videogames
Videogames(title="Stray", genre="Adventure", year_released=2022).save()
Videogames(title="Beyond", genre="Adventure", year_released=2013).save()
Videogames(title="The Legend of Zelda: Ocarina of Time", genre="Action", year_released=1998).save()

print("test data successfully updated")

