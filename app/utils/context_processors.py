from decouple import config


def site_settings(request):
    return {'SECRET_ADMIN_URL': config('SECRET_ADMIN_URL'),
            'LMS_USER': request.user.groups.filter(name='LMS').exists() or request.user.is_superuser,}