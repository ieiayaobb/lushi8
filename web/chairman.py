# -*- coding:utf-8 -*-

class Chairman:
    def __init__(self):
        self.title = ''
        self.name = ''
        self.href = ''
        self.img = ''
        self.num = ''
        self.desc = ''

    def __repr__(self):
        return "[" + self.title + "]-[" + self.name + "]-[" + self.href + "]-[" + self.img + "]-[" + self.num + "]-[" + self.desc + "]"