from django.db import models

# Create your models here.
class trails(models.Model):
    email = models.EmailField()
    stocks = models.CharField(max_length=456)