# coding=utf-8
from __future__ import unicode_literals

import json

from redisco import models

import redisco

from lushi.settings import REDIS_HOST, REDIS_DB, REDIS_PASSWORD

redisco.connection_setup(host=REDIS_HOST, db=REDIS_DB, password=REDIS_PASSWORD)
# redisco.connection_setup(host='127.0.0.1', db=7)

# Create your models here.
# class Chairman(models.Model):
#     # id = models.CharField(primary_key=True, max_length=128)
#     title = models.CharField(max_length=128)
#     name = models.CharField(max_length=128)
#     href = models.TextField(max_length=2048)
#     img = models.TextField(max_length=2048)
#     num = models.IntegerField()
#     desc = models.TextField(max_length=2048)
#     type = models.CharField(max_length=128)
#     avatar = models.TextField(max_length=2048)
#
#     def set_num(self, num):
#         if '万' in num:
#             self.num = round(float(num.replace('万','').replace('\r', '').replace('\n', '')) * 10000)
#         else:
#             self.num = int(num)
#
#     def __repr__(self):
#         return "[" + self.type + "]-[" + self.title + "]-[" + self.name + "]-[" + self.href + "]-[" + self.img + "]-[" + self.avatar + "]-[" + self.num + "]-[" + self.desc + "]"


class Chairman(models.Model):
    id = models.Attribute(unique=True)
    # pk = models.Attribute(unique=True)
    title = models.Attribute()
    name = models.Attribute()
    href = models.Attribute()
    img = models.Attribute()
    num = models.IntegerField()
    desc = models.Attribute()
    type = models.Attribute()
    avatar = models.Attribute()

    object_name = 'chairman'

    def __init__(self, *args, **kwargs):
        super(Chairman, self).__init__(**kwargs)
        if 'ele' in kwargs:
            ele = json.loads(kwargs['ele'])
            self.id = ele['_id']
            self.title = ele['_title']
            self.name = ele['_name']
            self.href = ele['_href']
            self.num = ele['_num']
            self.img = ele['_img']
            self.desc = ele['_desc']
            self.type = ele['_type']
            self.avatar = ele['_avatar']

    def set_id(self, id):
        self.pk = id
        self.id = id

    def set_num(self, num):
        if '万' in num:
            self.num = int(round(float(num.replace('万','').replace('\r', '').replace('\n', '')) * 10000))
        else:
            self.num = int(num)

    def __unicode__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
        # uni = "[" + self.__getattribute__('id') + "]"
        # if self.title:
        #     uni += "-[" + self.__getattribute__('title') + "]"
        # if self.name:
        #     uni += "-[" + self.__getattribute__('name') + "]"
        # if self.href:
        #     uni += "-[" + self.__getattribute__('href') + "]"
        # if self.img:
        #     uni += "-[" + self.__getattribute__('img') + "]"
        # if self.avatar:
        #     uni += "-[" + self.__getattribute__('avatar') + "]"
        # if self.num:
        #     uni += "-[" + str(self.__getattribute__('num')) + "]"
        # if self.desc:
        #     uni += "-[" + self.__getattribute__('desc') + "]"
        #
        # return uni