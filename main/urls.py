from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include the URLs of the allauth app
    path('', include('app.urls')),  # Include the URLs of your new app
]