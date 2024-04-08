from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('',views.login,name='login'),
path('signup',views.signup,name='signup'),
path('create',views.create,name='create'),
path('send',views.send,name='send'),
path('show',views.show,name='show'),
path('get',views.get,name='get'),
path('stat',views.stat,name='stat'),
path('delete',views.delete_task,name='delete'),
path('edit',views.edit,name='edit'),
path('tp',views.tp,name='tp'),
path('dashboard',views.dashboard,name='dashboard'),

path('navbar',views.navbar,name='navbar'),

path('RecordEdited',views.RecordEdited,name='record'),
]