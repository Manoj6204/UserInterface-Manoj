from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    rollno = models.IntegerField(unique=True)
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.name
