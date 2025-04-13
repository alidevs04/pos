from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default = 0)
    category = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name