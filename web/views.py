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
from web.models import Chairman
from web.serializers import ChairmanSerializer
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'chairmans': reverse('chairman-list', request=request, format=format),
    })


def _convert_chairman(ele):
    chairman = Chairman(ele=ele)
    return chairman


def get_index(request):
    # response = requests.get('http://127.0.0.1:8000/api/chairmans/')
    # chairmans = response.json()

    if 'type' in request.GET:
        type = request.GET['type']
        chairmans = Chairman.objects.filter(type=type).order('-num')
    else:
        chairmans = Chairman.objects.all().order('-num')

    # chairmans_set = SortedSet('chairmans_set')
    # chairmans_hash = SortedSet('chairmans_hash')
    # chairmans = map(_convert_chairman, chairmans_set.revmembers)
    # chairmans = map(_convert_chairman, chairmans_hash.members)

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

    # chairmans_set = SortedSet('chairmans_set')
    # charimans_hash = Hash('chairmans_hash')
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


class ChairmanViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ChairmanSerializer
    lookup_field = ('id')

    def get_queryset(self):
        return Chairman.objects.all().order('-num')

    def retrieve(self, request, *args, **kwargs):
        chairman = Chairman(id=kwargs['id'])
        serializer = self.get_serializer(chairman)
        return Response(serializer.data)

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
