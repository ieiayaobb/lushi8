import logging

import datetime
import os

import kronos
import redis
from django.core.cache import cache
import time

import web

from web.fetch import Fetcher

logger = logging.getLogger(__name__)

@kronos.register('0 */1 * * *')
def refresh_rank():
    redis_instance = redis.StrictRedis(host='10.66.183.211', db=7, password='crs-qqptkhei:sanpang315')
    redis_instance.delete("Chairman:*")

    fetcher = Fetcher()
    fetcher.fetch_cc()
    fetcher.fetch_douyu()
    fetcher.fetch_longzhu()
    fetcher.fetch_quanmin()
    fetcher.fetch_xiongmao()
    fetcher.fetch_zhanqi()
    fetcher.fetch_huya()

    for chairman in fetcher.chairmans:
        if chairman.is_valid():
            chairman.save()
        else:
            print chairman.errors