from django.shortcuts import render
from django.utils import timezone
from .forms import GlazingProjectForm
from .models import Windows, Glazing_Project

def glazing_project_list(request):
    glazing_projects_query_set = Glazing_Project.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'glazing/glazing_project_list.html', {'glazing_projects_query_set' : glazing_projects_query_set})

def glazing_project_new(request):
    form = GlazingProjectForm()
    return render(request, 'glazing/glazing_project_edit.html', {'form': form})