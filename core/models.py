from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    ranking = models.IntegerField()
    profession = models.CharField(max_length=200)
    image = models.ImageField()
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    def __str__(self):
        return self.last_face