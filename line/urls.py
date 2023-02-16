from django.urls import path
from .views import get_all_lines, create_line, update_line

urlpatterns = [
    path('all', get_all_lines),
    path('create', create_line),
    path('update/<int:id>', update_line)
]
