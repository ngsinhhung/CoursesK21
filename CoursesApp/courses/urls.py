from .admin import admin_site
from django.urls import path

urlpatterns = [
    path('admin/', admin_site.urls)
]