# api/admin.py
from django.contrib import admin
from .models.product import Product
from .models.cart import Cart
from .models.login_user import LoginUser

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(LoginUser)

