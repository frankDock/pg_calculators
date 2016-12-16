from glazing.forms import *
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import GlazingProjectForm, WindowsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

import json

@csrf_protect
def register(request):
    profile = ""
    c = RequestContext(request)

    def failure(errs):
        return HttpResponseServerError(
            json.dumps({'alert': render_to_string('registration/signup_failure.html', c),
                        'errors': errs})
            )
    if request.method == 'POST':

        # print(RegistrationForm(request.POST))
        user_form = UserForm(request.POST)
        if user_form.clean() != True:
            return failure(user_form.clean())
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid():

            user = User.objects.create_user(
                username=user_form.data['username'],
                password=user_form.data['password1'],
                email=user_form.data['email']
            )

            # profile_form.user = user.id
            # profile_form.company = user_form.data['company']
            # profile_form.save()
            UserProfile.objects.create(
                company = user_form.data['company'],
                user = user
            )

            # return HttpResponseRedirect('/register/success/')

            return HttpResponseRedirect('/register/done/')
        else:
            error = ""
            for field in user_form:
                if field.errors != []:
                    error = field.errors
            return failure(error)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        for field in profile_form:
            if field.name == 'company':
                profile = field
        # profile_form.user = False

    return render(request, 'registration/register.html', {'user_form': user_form, 'profile': profile})
    # return render_to_response('registration/register.html',{'form': form, 'request': request}, RequestContext(request))

def welcome(request):
    c = RequestContext(request)
    return render_to_response('registration/welcome.html', c)


@login_required
def glazing_project_list(request):
    glazing_projects_query_set = Glazing_Project.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'glazing/glazing_project_list.html', {'glazing_projects_query_set' : glazing_projects_query_set})

@login_required
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

@login_required
def glazing_project_detail(request, glazing_project_id):
    windows_query_set = Windows.objects.filter(glazing_project_id = glazing_project_id)
    detail = get_object_or_404(Glazing_Project, pk=glazing_project_id)

    total_area = windows_query_set.aggregate(Sum('window_area'))
    total_shgc_proposed = windows_query_set.aggregate(Sum('shgc_proposed'))
    total_conductance = windows_query_set.aggregate(Sum('conductance'))

    net_glazed_area_to_floor_area_ratio = 0

    if total_area.get('window_area__sum') is not None:
        net_glazed_area_to_floor_area_ratio = round(float(total_area.get('window_area__sum')) / float(detail.nett_floor_area),2)

    return render(request, 'glazing/glazing_project_detail.html', {
        'windows_query_set' : windows_query_set,
        'detail': detail, 'total_area': total_area,
        'total_shgc_proposed': total_shgc_proposed,
        'total_conductance': total_conductance,
        'net_glazed_area_to_floor_area_ratio': net_glazed_area_to_floor_area_ratio
    })

@login_required
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

@login_required
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

@login_required
def windows_detail(request, windows_id):
    detail = get_object_or_404(Windows, pk=windows_id)
    return render(request, 'glazing/windows_detail.html', {'detail': detail})

@login_required
def windows_edit(request, pk):
    post = get_object_or_404(Windows, pk=pk)
    #form_class = WindowsForm
    if request.method == "POST":
        form = WindowsForm(request.POST,instance=post )
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # import pdb; pdb.set_trace()
            return redirect('glazing:glazing_project_detail', glazing_project_id = post.glazing_project_id.pk)

    else:
        form = WindowsForm(instance=post)


    return render(request, 'glazing/windows_edit.html', {'form': form})

@login_required
def climate_map(request):

    return render(request, 'glazing/climate_map.html', {})

@login_required
def climate_map(request):

    return render(request, 'glazing/climate_map.html', {})

