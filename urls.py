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
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import serializers, viewsets, routers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.routers import DefaultRouter, BaseRouter, SimpleRouter

import web.urls

# Serializers define the API representation.
from web import views

#
# class RediscoRouter(DefaultRouter):
#     def get_default_base_name(self, viewset):
#         return viewset.queryset.model_class.object_name.lower()
#
# router = RediscoRouter()
# router.register(r'chairmans', views.ChairmanViewSet)


from django.views import static


urlpatterns = [
    # url(r'^api/', include(router.urls)),

    url(r'^', include(web.urls)),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': 'static'}),
    # url(r'^api/$', views.api_root),
    # url(r'^api/chairmans/$', chairman_list, name='chairman-list'),
    # url(r'^api/chairmans/(?P<id>[A-Za-z0-9_]+)/$', chairman_detail, name='chairman-detail'),
    #
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
