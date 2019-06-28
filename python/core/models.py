from django.db import models

# Create your models here.
class Consumer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()

    def ___str___(self):
        return self.nome
