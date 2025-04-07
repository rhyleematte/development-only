from django.urls import path, include
from django.contrib import admin
from .views import HelloWorld, Students, ContactListView
from .exam_views import ChatListCreateView  # Ensure this exists

# Ecommerce
from . import views  # Import views herec
from .views import CartViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register the CartViewSet
router = DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')
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
    path('cart/add/', CartViewSet.as_view({'post': 'add_to_cart'}), name='add_to_cart'),
    path('cart/checkout/', CartViewSet.as_view({'post': 'checkout'}), name='checkout'),
    #End ecommerce
]