from django.db import models

class Club(models.Model):
    name=models.CharField(max_length=15)
    money=models.IntegerField()


    def __str__(self) -> str:
        return self.name
