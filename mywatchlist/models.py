from logging.handlers import WatchedFileHandler
from django.db import models

# Create your models here.
class MyWatchList(models.Model):
    watched = models.CharField(max_length=50)
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()

