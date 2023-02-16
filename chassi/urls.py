from django.urls import path
from .views import get_all_chassis, create_chassi, update_chassi, get_all_chassis_within_search

urlpatterns = [
    path('all', get_all_chassis),
    path('create', create_chassi),
    path('update/<int:id>', update_chassi),
    path('search/', get_all_chassis_within_search)
]
