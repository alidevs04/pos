from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.timezone import now

# Create your models here.
class Order(models.Model):
    order_num = models.IntegerField()
    order_items = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    order_date = models.DateField(now().date(), auto_now_add=True)
    total_price = models.IntegerField()


    def __str__(self):
        return self.name