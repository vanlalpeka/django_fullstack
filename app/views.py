from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import Note

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User


# def landing_page(request):
#     return render(request, 'app/landing_page.html')

# def note_list(request):
#     notes = Note.objects.all()
#     return render(request, 'app/note_list.html', {'notes': notes})

# def note_detail(request, note_id):
#     note = Note.objects.get(id=note_id)
#     return render(request, 'app/note_detail.html', {'note': note})

def custom_logout_view(request):
    logout(request)
    return redirect('landing_page')

class LandingPageView(TemplateView):
    template_name = 'app/landing_page.html'

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'app/note_list.html'
    context_object_name = 'notes'

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'app/note_detail.html'
    context_object_name = 'note'

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'app/profile.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)