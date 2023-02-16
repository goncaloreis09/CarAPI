from django.urls import path
from .views import get_all_groups, create_group

urlpatterns = [
    path('all', get_all_groups),
    path('create', create_group)
]
