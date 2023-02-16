from django.urls import path
from .views import list_brands, create_brand, delete_brand, update_brand, list_searched_brands

urlpatterns = [
    path('all', list_brands),
    path('create', create_brand),
    path('delete/<int:id>', delete_brand),
    path('update/<int:id>', update_brand),
    path('search/', list_searched_brands)
]
