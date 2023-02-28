from django.contrib import admin
from .models import Profile
from .models import Sell, category, brand,Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Sell)
admin.site.register(category)
admin.site.register(brand)
admin.site.register(Comment)
