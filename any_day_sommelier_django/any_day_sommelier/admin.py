from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Wine, Food, User, Pairing, Favorite

admin.site.register(Wine)
admin.site.register(Food)
admin.site.register(User)
admin.site.register(Pairing)
admin.site.register(Favorite)