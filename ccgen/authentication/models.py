from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.username
