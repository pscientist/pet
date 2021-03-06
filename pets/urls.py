from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'pets'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/blog/$', views.BlogView.as_view(), name='blog'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    url(r'^(?P<pk>[0-9]+)/api/$', views.ApiDetails.as_view(), name='api_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)