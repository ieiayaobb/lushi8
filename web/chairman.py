# -*- coding:utf-8 -*-

class Chairman:
    def __init__(self):
        self.title = ''
        self.name = ''
        self.href = ''
        self.img = ''
        self.num = ''
        self.desc = ''
        self.type = ''
        self.avatar = ''

    def __repr__(self):
        return "[" + self.type + "]-[" + self.title + "]-[" + self.name + "]-[" + self.href + "]-[" + self.img + "]-[" + self.avatar + "]-[" + self.num + "]-[" + self.desc + "]"