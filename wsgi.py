# coding: utf-8

from gevent import monkey
monkey.patch_all()

import os
# 设置 Django 项目配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from gevent.pywsgi import WSGIServer

from cloud import engine

application = engine


if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    server = WSGIServer(('localhost', PORT), application)
    server.serve_forever()
