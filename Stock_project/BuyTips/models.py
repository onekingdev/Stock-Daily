from django.db import models

# Create your models here.


class Tips(models.Model):
    stock_name = models.CharField(max_length=50)
    buy_price = models.CharField(max_length=400)
    target_price = models.CharField(max_length=300)
    sl_price = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.stock_name} | Buy At {self.buy_price} | Target {self.target_price} | Sl At {self.sl_price}"
class UserEmail(models.Model):
    email = models.EmailField(max_length=200)