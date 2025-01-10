from django.shortcuts import render
from .models import Note

def landing_page(request):
    return render(request, 'app/landing_page.html')

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'app/note_list.html', {'notes': notes})

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, 'app/note_detail.html', {'note': note})