from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import GlazingProjectForm
from .models import Windows, Glazing_Project

def glazing_project_list(request):
    glazing_projects_query_set = Glazing_Project.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'glazing/glazing_project_list.html', {'glazing_projects_query_set' : glazing_projects_query_set})

def glazing_project_new(request):
    if request.method == "POST":
            form = GlazingProjectForm(request.POST)
            if form.is_valid():
                    post = form.save(commit=False)
                    post.pub_date = timezone.now()
                    post.save()
                    return redirect('glazing:glazing_project_detail', glazing_project_id = post.pk)
    else:    
            form = GlazingProjectForm()
    return render(request, 'glazing/glazing_project_edit.html', {'form': form})

def glazing_project_detail(request, glazing_project_id):
    detail = get_object_or_404(Glazing_Project, pk=glazing_project_id)
    return render(request, 'glazing/glazing_project_detail.html', {'detail': detail})

def glazing_project_edit(request, pk):
    post = get_object_or_404(Glazing_Project, pk=pk)
    if request.method == "POST":
        form = GlazingProjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('glazing:glazing_project_detail', glazing_project_id = post.pk)
    else:
        form = GlazingProjectForm(instance=post)
    return render(request, 'glazing/glazing_project_edit.html', {'form': form})
