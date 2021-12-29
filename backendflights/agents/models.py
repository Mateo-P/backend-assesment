from django.db import models

class Agent(models.Model):
    id = models.CharField(primary_key=True, max_length=2)
    name = models.CharField(max_length=32)
    rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.id}'
