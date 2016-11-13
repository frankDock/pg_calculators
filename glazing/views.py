from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import GlazingProjectForm, WindowsForm
from .models import *
#import pdb; pdb.set_trace()

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
    windows_query_set = Windows.objects.filter(glazing_project_id = glazing_project_id)
    detail = get_object_or_404(Glazing_Project, pk=glazing_project_id)
    return render(request, 'glazing/glazing_project_detail.html', {
        'windows_query_set' : windows_query_set,
        'detail': detail,
    })

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

def windows_new(request, glazing_project_id):
    if request.method == "POST":
            form = WindowsForm(request.POST)
            if form.is_valid():
                    post = form.save(commit=False)
                    post.window_area = post.width * post.height
                    post.save()
                    return redirect('glazing:windows_detail', windows_id = post.pk)
    else:    
            form = WindowsForm(initial={'glazing_project_id': glazing_project_id})
    return render(request, 'glazing/windows_edit.html', {'form': form})

def windows_detail(request, windows_id):
    detail = get_object_or_404(Windows, pk=windows_id)
    return render(request, 'glazing/windows_detail.html', {'detail': detail})

def windows_edit(request, pk):
    post = get_object_or_404(Windows, pk=pk)
    if request.method == "POST":
        form = WindowsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('glazing:windows_detail', windows_id = post.pk)
    else:
        form = WindowsForm(instance=post)
    return render(request, 'glazing/windows_edit.html', {'form': form})
