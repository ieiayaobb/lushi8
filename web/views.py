import requests
from django.http import Http404
from django.shortcuts import render, render_to_response


# Create your views here.
from django.template import RequestContext
from redis import ResponseError
from redisco.containers import Set, SortedSet, Hash
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from web.fetch import Fetcher
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

import leancloud

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'chairmans': reverse('chairman-list', request=request, format=format),
    })


def get_index(request):
    # response = requests.get('http://127.0.0.1:8000/api/chairmans/')
    # chairmans = response.json()

    leancloud.init("zeDAC8hXWeaccjdYd3K42OOG-gzGzoHsz", "2pUtBJhLoxTTSaSoETQb4qfA")

    # Chairman = leancloud.Object.extend('Chairman')
    query = leancloud.Query('Chairman')

    chairmans = []

    for chairman in query.add_descending('num').find():
        chairmans.append(chairman.attributes)

    return render_to_response('index.html', locals(),
                              context_instance=RequestContext(request))


def fetch(request):
    fetcher = Fetcher()
    fetcher.fetch_cc()
    fetcher.fetch_douyu()
    fetcher.fetch_longzhu()
    fetcher.fetch_quanmin()
    fetcher.fetch_xiongmao()
    fetcher.fetch_zhanqi()
    fetcher.fetch_huya()

    for chairman in fetcher.chairmans:
        try:
            if chairman.is_valid():
                # charimans_hash[chairman.id] = chairman
                # chairmans_set.add(chairman, chairman.num)
                chairman.save()
            else:
                print chairman.errors
        except Exception, e:
            print e

    return render_to_response('index.html', locals(),
                              context_instance=RequestContext(request))


# class ChairmanList(generics.ListAPIView):
#     queryset = Chairman.objects.all().order('-num')
#     serializer_class = ChairmanSerializer
#
#
# class ChairmanDetail(mixins.RetrieveModelMixin,
#                      generics.GenericAPIView):
#     queryset = Chairman.objects.all()
#     serializer_class = ChairmanSerializer
#     lookup_field = ('id')
#
#     def get(self, request, *args, **kwargs):
#         chairman = Chairman(id=kwargs['id'])
#         serializer = self.get_serializer(chairman)
#         return Response(serializer.data)
