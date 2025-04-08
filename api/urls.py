from django.urls import path, include
from django.contrib import admin
from .views import HelloWorld, Students, ContactListView
from .exam_views import ChatListCreateView  # Ensure this exists
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.product import Product
from .models.cart import Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework.routers import DefaultRouter
from .views import CartViewSet
# Ecommerce
from . import views  # Import views herec
from .views import CartViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register the CartViewSet
router = DefaultRouter()
router.register(r'cart', CartViewSet)
urlpatterns = router.urls
# End Ecommerce

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('contact/', ContactListView.as_view(), name='contact_new'),
    path('students/', Students.as_view(), name='list_students'),
    path('chat/', ChatListCreateView.as_view(), name='chat_view'),  # Keep this
    path('exam/', include('api.exam_urls')),
    path('admin/', admin.site.urls),
    #Ecommerce
    path('products/', views.product_list, name='product_list'),
    path('cart/', CartViewSet.as_view({'get': 'list'})),
    # Include the API router for cart-related API endpoints
    path('api/', include(router.urls)),
    #End ecommerce
]