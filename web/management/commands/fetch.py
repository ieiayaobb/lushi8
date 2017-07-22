# -*- coding: utf-8 -*-
import sys
from web.fetch import Fetcher
from django.core.management.base import BaseCommand
import leancloud
from settings import LEAN_CLOUD_ID, LEAN_CLOUD_SECRET

reload(sys)
sys.setdefaultencoding("utf-8")

class Command(BaseCommand):
    def handle(self, *args, **options):
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
