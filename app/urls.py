from django.urls import path
from .views import LandingPageView, NoteDetailView, custom_logout_view, UserProfileDetailView, NoteListView
from . import ajax_datatable_views

urlpatterns = [
    path('ajax_datatable/notes/', ajax_datatable_views.NoteAjaxDatatableView.as_view(),name="ajax_datatable_notes"),

    path('', LandingPageView.as_view(), name='landing_page'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('logout/', custom_logout_view, name='custom_logout'),
    path('profile/', UserProfileDetailView.as_view(), name='profile'),
    path('notes/<str:pk>/', NoteDetailView.as_view(), name='note_detail'),
]