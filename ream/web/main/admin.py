from django.contrib import admin
from .models import *

# admin.site.register(News)
#
# admin.site.register(Contacts)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('id', 'title', 'image', 'description', 'author')
    readonly_fields = ('id',)
    list_display = ('title', 'slug')


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    fields = ('id', 'title')
    readonly_fields = ('id', )
    list_display = ('title', 'slug')