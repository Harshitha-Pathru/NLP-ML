from django.db import models

class User(models.Model):
    username=models.charField(max_length=100)
    email=models.EmailField()
    
    def __str__(self):
        return self.username

