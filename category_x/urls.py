from django.conf.urls import url

from . import views

app_name = 'category_x'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<template_name>.+)$', views.static_render, name='static_render'),
]