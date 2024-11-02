# simulation/urls.py
from django.urls import path
from .views import simulate, index_view

urlpatterns = [
    path('', index_view, name='index'),  # Serve https://127.0.0.1:8000
    path('simulate/', simulate, name='simulate'),  # Serve https://127.0.0.1:8000/simulate
]