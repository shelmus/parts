from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.search_parts, name='search_parts'),
    url(r'^new/$', views.new_parts, name='new_parts'),
    url(r'^part/(?P<part_id>.*)', views.part_detail, name='part_detail'),
    url(r'^remove/(?P<part_id>.*)', views.remove_part, name='remove_part'),
]
