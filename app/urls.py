from django.urls import path
from .views import landing_page, list_notes

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('notes/', list_notes, name='list_notes'),
]