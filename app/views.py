# filepath: /home/peka/django_fullstack/myapp/views.py
from django.shortcuts import render

def landing_page(request):
    return render(request, 'app/landing_page.html')