from django.db import models

class Vinyls(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=200)
    tracks = models.IntegerField()
    
    def __str__(self):
      return f"{self.title}, {self.artist}, {self.tracks}, {self.id}"

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    year_published = models.IntegerField()
    
    def __str__(self):
      return f"{self.title}, {self.author}, {self.year_published}, {self.id}"

class Videogames(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    year_released = models.IntegerField()
    
    def __str__(self):
      return f"{self.title}, {self.genre}, {self.year_released}, {self.id}"
