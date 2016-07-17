import requests
from django.shortcuts import render, render_to_response


# Create your views here.
from django.template import RequestContext

from web.fetch import Fetcher
from web.models import Chairman


def get_index(request):
    # response = requests.get('http://127.0.0.1:8000/api/chairmans/')
    # chairmans = response.json()
    chairmans = Chairman.objects.all().order('-num')
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

    for chairman in fetcher.chairmans:
        if chairman.is_valid():
            chairman.save()
        else:
            print chairman.errors

    return render_to_response('index.html', locals(),
                              context_instance=RequestContext(request))

