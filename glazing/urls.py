from django.conf.urls import url
from . import views

app_name = 'glazing'
urlpatterns = [
    url(r'^$', views.glazing_project_list, name='glazing_project_list'),
    url(r'^(?P<glazing_project_id>[0-9]+)/$', views.glazing_project_detail, name='glazing_project_detail'),
    url(r'^new/$', views.glazing_project_new, name='glazing_project_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.glazing_project_edit, name='glazing_project_edit'),
    url(r'^new_window/(?P<glazing_project_id>[0-9]+)/$', views.windows_new, name='windows_new'),
    url(r'^windows/(?P<windows_id>[0-9]+)/$', views.windows_detail, name='windows_detail'),
    url(r'^windows/(?P<pk>[0-9]+)/edit/$', views.windows_edit, name='windows_edit'),
    url(r'^climate-map/$', views.climate_map, name='climate_map'),
]

