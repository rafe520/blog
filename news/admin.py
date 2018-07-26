from django.contrib import admin
from .models import Category
from .models import News


admin.site.register(Category)
admin.site.register(News)
