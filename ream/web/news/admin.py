from django.contrib import admin
from .models import FavouriteNews
# Register your models here.


@admin.register(FavouriteNews)
class FavoriteNewsAdmin(admin.ModelAdmin):
    pass