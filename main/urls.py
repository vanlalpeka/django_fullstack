from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include the URLs of the allauth app
    # path('invitations/', include('invitations.urls', namespace='invitations')),  # Include the URLs of the invitations app
    path('', include('app.urls')),  # Include the URLs of your new app
]