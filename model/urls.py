from django.urls import path
from .views import get_all_models, create_model

urlpatterns = [
    path('all', get_all_models),
    path('create', create_model)
]
