from django.conf.urls import url

from . import views

app_name = 'glazing'
urlpatterns = [
    url(r'^$', views.glazing_project_list, name='glazing_project_list'),
    #url(r'^glazing/(?P<pk>\d+)/$', views.glazing_project_detail, name='glazing_project_detail'),
    #url(r'^glazing/new/$', views.glazing_project_new, name='glazing_project_new'),
]

