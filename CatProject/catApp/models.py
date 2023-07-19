from django.db import models

# Create your models here.
class CatShop(models.Model):
    name = models.CharField(max_length=100)
    # positive integer field
    price = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    discription = models.TextField()

    def __str__(self):
        return self.name
