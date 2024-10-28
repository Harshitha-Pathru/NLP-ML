from django.db import models

class User(models.Model):
    username=models.charField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return self.username

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    genre =  models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title



