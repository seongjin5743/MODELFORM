from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    # READ
    path('',views.index, name='index'),

    # CREATE
    path('create/', views.create, name='create')
]
