# -*- coding: utf-8 -*-

import sys

from web.fetch import Fetcher
from web.models import *
from django.core.management.base import BaseCommand

reload(sys)
sys.setdefaultencoding("utf-8")

class Command(BaseCommand):
    def handle(self, *args, **options):
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

