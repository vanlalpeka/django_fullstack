from django.urls import path
from .views import LandingPageView, custom_logout_view, CustomUserUpdateView, NoteListView, DashboardView
from . import ajax_datatable_views

urlpatterns = [
    path('ajax_datatable/notes/', ajax_datatable_views.NoteAjaxDatatableView.as_view(),name="ajax_datatable_notes"),

    path('', LandingPageView.as_view(), name='landing_page'),
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('logout/', custom_logout_view, name='custom_logout'),
    path('profile/<int:pk>/', CustomUserUpdateView.as_view(), name='profile'),
    # path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),    
]