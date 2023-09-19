from django.contrib import admin
from . import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Comment)
class BlogAdmin(admin.ModelAdmin):
    pass
