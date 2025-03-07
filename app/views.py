from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
from .models import Note, Department

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User

import plotly.express as px
import pandas as pd

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

class NoteListView(LoginRequiredMixin, TemplateView):
    template_name = 'app/note_list.html'

class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'app/note_detail.html'
    context_object_name = 'note'

    # def get(self, request, pk, *args, **kwargs):        
    #     template = 'app/note_detail.html'
    #     print(Note.objects.get(pk=pk))
    #     return render(request, template, context={'note': Note.objects.get(pk=pk)})



class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'app/profile.html'
    context_object_name = 'profile'

    def get_queryset(self):
        return User.objects.get(id=self.request.user.id)
    
class DashboardView(LoginRequiredMixin, DetailView):
    # model = Note
    # template_name = 'app/dashboard.html'
    context_object_name = 'dashboard'

    def get(self, request):        
        template = 'app/dashboard.html'
        df = pd.DataFrame(list(Note.objects.all().values()))
        dpt = list(Department.objects.all().values())
        # print(dpt)
        # Group by concerned_department and count occurrences
        department_counts = df['concerned_department_id'].value_counts().reset_index()
        department_counts.columns = ['concerned_department_id', 'count']
        department_counts["concerned_department"] = department_counts["concerned_department_id"].map({d['id']: d['name'] for d in dpt})	

        # Create a horizontal bar chart
        fig1 = px.bar(department_counts, 
                    x='count', 
                    y='concerned_department', 
                    orientation='h',
                    text='count',  # Show count on the bars
                    title="Notes per Concerned Department",
                    labels={'count': 'Number of Notes', 'concerned_department': 'Department'})
        fig1.update_layout(margin=dict(l=0, r=0))



        # Group by date and count occurrences
        df['month'] = pd.to_datetime(df['date'])
        df['month'] = df['month'].dt.strftime('%Y-%b')
        month_counts = df['month'].value_counts().reset_index().sort_values('month')
        month_counts.columns = ['month', 'count']
        # print(month_counts)

        # Line chart: Notes over Time
        fig2 = px.line(month_counts,
                    x='month',
                    y='count',
                    markers=True,
                    text='count',  # Show count on the bars
                    title='Notes per month',
                    labels={'month': 'Month', 'count': 'Number of Notes'})
        
        # Position the text labels above the points
        fig2.update_traces(textposition='top center')
        fig2.update_layout(margin=dict(l=0, r=0))


        
        # plots = [fig1.to_html(full_html=False), fig2.to_html(full_html=False)]

        return render(request, template, 
                    #   context={"fig1": fig1.to_html(full_html=False, config={'displaylogo': False}, include_plotlyjs=False),
                    #            "fig2": fig2.to_html(full_html=False, config={'displaylogo': False}, include_plotlyjs=False)})
                      context={"fig1": fig1.to_html(full_html=False, config={'displaylogo': False}),
                               "fig2": fig2.to_html(full_html=False, config={'displaylogo': False})})