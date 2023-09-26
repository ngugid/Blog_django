from django.db import models


# Create your models here.
class Blog1(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)

    def __str__(self):
        return self.title