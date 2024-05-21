from django.contrib import admin
from . import models


# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "price",
    ]


class MenuAdmin(admin.ModelAdmin):
    list_display = [
        "type",
    ]


admin.site.register(models.Food, FoodAdmin)
admin.site.register(models.Menu, MenuAdmin)
