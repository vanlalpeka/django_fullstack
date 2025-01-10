from django.shortcuts import render
from .models import Note

def landing_page(request):
    return render(request, 'app/landing_page.html')

def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'app/list_notes.html', {'notes': notes})