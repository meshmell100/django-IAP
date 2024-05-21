from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Food(models.Model):
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)
    name = models.CharField(_("Name"), max_length=50)
    price = models.DecimalField(_("Price"), decimal_places=2, max_digits=4)

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)
    MENU_TYPES = [
        ("B", "Breakfast"),
        ("BR", "Branch"),
        ("L", "Lunch"),
        ("S_B", "Snacks & Bev"),
        ("D", "Dinner"),
    ]
    type = models.CharField(
        _("Type of Menu"), max_length=50, choices=MENU_TYPES, default="B"
    )
    foods = models.ManyToManyField(
        "menu.Food", verbose_name=_("Foods"), related_name="menus"
    )

    def __str__(self) -> str:
        return self.type
