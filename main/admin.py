from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'website_link', 'director', 'schedule', 'price', 'duration')
    fields = ('title', 'poster', 'details', 'website_link', 'director')


admin.site.register(Movie)
