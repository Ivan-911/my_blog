"""Определяем схемы URL для blogs"""

from django.urls import path, re_path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notes/', views.notes, name='notes'),
    re_path(r'^notes/(?P<note_id>\d+)/$', views.note, name='note'),
    path('new/', views.new, name='new'),
    re_path(r'^edit_blog/(?P<note_id>\d+)/$', views.edit_blog, name='edit_blog')
]
