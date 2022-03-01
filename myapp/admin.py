from django.contrib import admin

from .models.category import Category
from .models.city import City
from .models.news import News


admin.site.register(Category)
admin.site.register(City)
admin.site.register( News)