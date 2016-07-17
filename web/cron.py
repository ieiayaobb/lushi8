import logging

import datetime
import os

import kronos
from django.core.cache import cache
import time

import web

from web.fetch import Fetcher

logger = logging.getLogger(__name__)

@kronos.register('*/1 * * * *')
def refresh_rank():
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