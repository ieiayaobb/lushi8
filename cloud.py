# coding: utf-8
import leancloud
from django.core.wsgi import get_wsgi_application
from leancloud import Engine, LeanEngineError

from web.fetch import Fetcher

engine = Engine(get_wsgi_application())

@engine.define
def fetch(**params):
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

@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')
