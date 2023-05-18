from django.db import models

# Create your models here.

class TypesList(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Type(models.Model):
    typeslist = models.ForeignKey(TypesList, on_delete=models.CASCADE)
    typing = models.CharField(max_length=1000)
    winner = models.BooleanField()

    def __str__(self):
        return self.typing