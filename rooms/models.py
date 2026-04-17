from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):

    room_number = models.CharField(max_length=12, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(max_length=20, default=False)

    def __str__(self) -> str:
        return self.room_number



