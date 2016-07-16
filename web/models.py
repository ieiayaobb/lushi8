# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Chairman(models.Model):
    # id = models.CharField(primary_key=True, max_length=128)
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    href = models.TextField(max_length=2048)
    img = models.TextField(max_length=2048)
    num = models.IntegerField()
    desc = models.TextField(max_length=2048)
    type = models.CharField(max_length=128)
    avatar = models.TextField(max_length=2048)

    def set_num(self, num):
        if '万' in num:
            self.num = round(float(num.replace('万','').replace('\r', '').replace('\n', '')) * 10000)
        else:
            self.num = int(num)

    def __repr__(self):
        return "[" + self.type + "]-[" + self.title + "]-[" + self.name + "]-[" + self.href + "]-[" + self.img + "]-[" + self.avatar + "]-[" + self.num + "]-[" + self.desc + "]"