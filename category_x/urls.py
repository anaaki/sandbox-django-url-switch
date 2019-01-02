from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<template_name>', views.static_render, name=''),
]