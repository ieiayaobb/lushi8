import requests
from django.http import Http404
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template import RequestContext

from web.fetch import Fetcher

from settings import LEAN_CLOUD_ID, LEAN_CLOUD_SECRET
import leancloud

# @api_view(('GET',))
# def api_root(request, format=None):
#     return Response({
#         'chairmans': reverse('chairman-list', request=request, format=format),
#     })


def get_index(request):
    # response = requests.get('http://127.0.0.1:8000/api/chairmans/')
    # chairmans = response.json()

    leancloud.init(LEAN_CLOUD_ID, LEAN_CLOUD_SECRET)

    # Chairman = leancloud.Object.extend('Chairman')
    query = leancloud.Query('Chairman')

    chairmans = []

    for chairman in query.add_descending('num').find():
        chairmans.append(chairman.attributes)

    return render_to_response('index.html', locals(),
                              context_instance=RequestContext(request))


def fetch(request):
    leancloud.init(LEAN_CLOUD_ID, LEAN_CLOUD_SECRET)

    query = leancloud.Query('Chairman')

    allDataCompleted = False
    batch = 0
    limit = 1000
    while not allDataCompleted:
        query.limit(limit)
        query.skip(batch * limit)
        query.add_ascending('createdAt')
        resultList = query.find()
        if len(resultList) < limit:
            allDataCompleted = True
            leancloud.Object.destroy_all(resultList)
        batch += 1

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
            chairman.save()
        except Exception, e:
            print e

    return redirect("/")
