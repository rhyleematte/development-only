from django.urls import path
from .exam_views import ChatListCreateView  # ✅ Ensure this is correctly imported

urlpatterns = [
    path('', ChatListCreateView.as_view(), name='chat-list-create'),  # ✅ Correct path
]