from django.contrib import admin

from .models import Category, Item, Basket, BasketItem

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Basket)
admin.site.register(BasketItem)

