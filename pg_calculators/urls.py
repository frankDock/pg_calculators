"""pg_calculators URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from glazing.views import *
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/glazing')),
    url(r'^glazing/', include('glazing.urls'), name='glazing'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/accounts/login'}, name='logout'),
    url(r'^accounts/password_reset/$', auth_views.password_reset, {'template_name': 'registration/forgotten.html','email_template_name':'registration/password_reset_email.html',"post_reset_redirect" : '/accounts/password_reset_done'}, name='password_reset'),
    url(r'^accounts/password_reset_done/$', auth_views.password_reset_done,{'template_name': 'registration/password_reset_done.html'}),

    url(r'^accounts/reset/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,{'template_name': 'registration/password_reset_confirm.html'}),
    url(r'^accounts/reset/done/$', auth_views.password_reset_complete,{'template_name': 'registration/password_reset_complete.html'}),
    url(r'^accounts/change-password/$', auth_views.password_change),
    url(r'^accounts/change-password/done/$', auth_views.password_change_done),

    url(r'^register/$', register, name='register'),
    url(r'^register/done/$', welcome, name='register-done'),

    # url(r'^accounts/reset/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,{'template_name': 'registration/password_reset_confirm.html'}),
    # url(r'^accounts/reset/done/$', auth_views.password_reset_complete,{'template_name': 'registration/password_reset_complete.html'}),

    # url(r'^register/password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.password_reset_confirm, {'template_name': 'registration/initial_confirm.html',
    #         'post_reset_redirect': 'accounts:register-complete',
    #     }, name='register-confirm'),
    # url(r'^register/complete/$', views.password_reset_complete, {'template_name': 'registration/initial_complete.html',}, name='register-complete'),
]


