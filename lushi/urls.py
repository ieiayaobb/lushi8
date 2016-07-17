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
from rest_framework import serializers, viewsets, routers

import web.urls

# Serializers define the API representation.
from web.models import Chairman


# class ChairmanSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Chairman
#         # fields = ('url', 'username', 'email', 'is_staff')
#
#
# # ViewSets define the view behavior.
# class ChairmanViewSet(viewsets.ModelViewSet):
#     queryset = Chairman.objects.all().order_by('-num')
#     serializer_class = ChairmanSerializer
#
#
# # Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'chairmans', ChairmanViewSet)


urlpatterns = [
    # url(r'^api/', include(router.urls)),
    url(r'^', include(web.urls)),

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
