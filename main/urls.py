from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include the URLs of the allauth app
    # path('invitations/', include('invitations.urls', namespace='invitations')),  # Include the URLs of the invitations app
    path('', include('app.urls')),  # Include the URLs of your new app
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()