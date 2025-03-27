from django.contrib import admin
from django.urls import include, path  # ✅ Correct import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ✅ Ensure this is correct
]
