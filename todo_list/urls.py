# Importing admin and include functions for URL routing
from django.contrib import admin
from django.urls import path, include

# Main URL configuration for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel accessible at /admin/
    path('', include('base.urls')),  # Include the URL patterns from the `base` app at the root URL
]
