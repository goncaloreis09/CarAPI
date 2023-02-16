from django.urls import path
from .views import get_all_engines, create_engine

urlpatterns = [
    path('all', get_all_engines),
    path('create', create_engine)
]
