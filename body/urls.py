from django.urls import path
from .views import get_all_bodies, create_body, update_body

urlpatterns = [
    path('all', get_all_bodies),
    path('create', create_body),
    path('update/<int:id>', update_body)
]
