from django.db import models

class CatFact(models.Model):
    fact = models.TextField()

    def __str__(self):
        return self.fact
