from decouple import config


def site_settings(request):
    return {'SECRET_ADMIN_URL': config('SECRET_ADMIN_URL')}