from django.contrib import admin
from .models import TechType, product, Review
# Register your models here.
admin.site.Register(TechType)
admin.site.Register(product)
admin.site.Register(Review)