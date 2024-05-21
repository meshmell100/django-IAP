from django.contrib import admin
from . import models


# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["food", "order", "quantity", "price"]


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "customer",
        "total_amount",
    ]


admin.site.register(models.OrderItem, OrderItemAdmin)
admin.site.register(models.Order, OrderAdmin)
