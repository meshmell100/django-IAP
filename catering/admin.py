from django.contrib import admin
from . import models
# Register your models here.
class PackageAdmin(admin.ModelAdmin):
    list_display = ["title", "description",]
admin.site.register(models.Package, PackageAdmin)
