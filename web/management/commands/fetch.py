# -*- coding: utf-8 -*-
import sys
from web.fetch import Fetcher
from django.core.management.base import BaseCommand
import leancloud

reload(sys)
sys.setdefaultencoding("utf-8")

class Command(BaseCommand):
    def handle(self, *args, **options):
        leancloud.init("zeDAC8hXWeaccjdYd3K42OOG-gzGzoHsz", "2pUtBJhLoxTTSaSoETQb4qfA")

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
