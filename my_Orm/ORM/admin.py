from django.contrib import admin
from .models import Movies, MovieAdmin
# Register your models here.

admin.site.register(Movies, MovieAdmin)
