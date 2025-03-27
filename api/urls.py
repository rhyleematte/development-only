from django.urls import path, include
from django.contrib import admin
from .views import HelloWorld, Students, ContactListView
from .exam_views import ChatListCreateView  # Ensure this exists

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('contact/', ContactListView.as_view(), name='contact_new'),
    path('students/', Students.as_view(), name='list_students'),
    path('chat/', ChatListCreateView.as_view(), name='chat_view'),  # Keep this
    path('exam/', include('api.exam_urls')),
    path('admin/', admin.site.urls),
]
