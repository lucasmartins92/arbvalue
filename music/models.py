from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=25)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + " - " + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title