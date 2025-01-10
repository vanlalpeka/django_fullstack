from django.urls import path
from .views import LandingPageView, NoteListView, NoteDetailView, custom_logout_view


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('logout/', custom_logout_view, name='custom_logout'),
    path('notes/<int:note_id>/', NoteDetailView.as_view(), name='note_detail'),
]