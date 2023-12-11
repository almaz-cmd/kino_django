from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/')
    details = models.TextField()
    website_link = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    session = models.CharField(max_length=100)

    def __str__(self):
        return self.title
