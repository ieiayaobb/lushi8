# -*- coding: utf-8 -*-

import sys

import redis as redis

from web.fetch import Fetcher
from web.models import *
from django.core.management.base import BaseCommand
import redis

reload(sys)
sys.setdefaultencoding("utf-8")


class Command(BaseCommand):
    def handle(self, *args, **options):
        redis_instance = redis.StrictRedis(host=REDIS_HOST, db=REDIS_DB, password=REDIS_PASSWORD)
        # redis_instance = redis.StrictRedis(host='127.0.0.1', db=7)
        for key in redis_instance.scan_iter("Chairman:*"):
            redis_instance.delete(key)

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
                    chairman.save()
                else:
                    print chairman.errors
            except Exception, e:
                print e
