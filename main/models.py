from django.db import models



class City(models.Model):
    city = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.city
