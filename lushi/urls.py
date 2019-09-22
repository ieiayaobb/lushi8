# coding=utf-8

"""lushi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import serializers, viewsets, routers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.routers import DefaultRouter, BaseRouter, SimpleRouter
from rest_framework import routers

# Serializers define the API representation.
from web import views

#
# class RediscoRouter(DefaultRouter):
#     def get_default_base_name(self, viewset):
#         return viewset.queryset.model_class.object_name.lower()
#
router = routers.DefaultRouter()
router.register(r'chairmans', views.ChairmanViewSet, base_name='chairmans')

from django.views import static
from web.views import get_index, fetch

urlpatterns = [
    # url(r'^api/', include(router.urls)),

    url(r'^$', get_index),
    url(r'^fetch/$', fetch),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),

    url(r'^api/', include(router.urls)),

    # url(r'^api/chairmans/$', fetcher.chairmans, name='chairman-list'),
    # url(r'^api/chairmans/(?P<id>[A-Za-z0-9_]+)/$', chairman_detail, name='chairman-detail'),
    #
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
