from django.urls import path
from .views import landing_page, note_list, note_detail, custom_logout_view

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('notes/', note_list, name='note_list'),
    path('logout/', custom_logout_view, name='custom_logout'),
    path('notes/<int:note_id>/', note_detail, name='note_detail'),
]