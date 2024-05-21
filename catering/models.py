from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Package(models.Model):
    created_at = models.DateTimeField(_("Date Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date Updated"), auto_now=True)
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    min_guests = models.IntegerField(_("Minimum number of guests"))
    max_guests = models.IntegerField(_("Maximum number of quests"))
    includes_appetizers = models.BooleanField(_("Includes Appetizers"), default=False)
    serving = models.BooleanField(_("Serving"), default=False)
    delivery = models.DecimalField(_("Price"), decimal_places=2, max_digits=8)

    def __str__(self):
        return self.title
