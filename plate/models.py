from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)
    customer = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.customer


class OrderItem(models.Model):
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey("menu.Food", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.food}-{self.quantity}"
