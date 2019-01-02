from django.urls import path

from . import views

app_name = 'category_x'
urlpatterns = [
    path('', views.index, name='index'),
    path('<template_name>', views.static_render, name='static_render'),
]