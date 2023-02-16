from django.urls import path
from .views import get_all_countries, create_country, update_country, get_countries_with_given_name

urlpatterns = [
    path('all', get_all_countries),
    #path('<slug:name>', get_countries_with_given_name),
    path('create', create_country),
    path('update/<int:id>', update_country)
]
