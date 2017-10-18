from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^admin/', admin.site.urls),
    url('^lineConnections/', views.findConnections, name='findConnections'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]