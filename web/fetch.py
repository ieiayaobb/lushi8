# -*- coding:utf-8 -*-

import json
import logging
import os
import re
import requests

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import leancloud

from settings import LEAN_CLOUD_ID, LEAN_CLOUD_SECRET

leancloud.init(LEAN_CLOUD_ID, LEAN_CLOUD_SECRET)

# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# urllib3.disable_warnings()
logging.captureWarnings(True)

class Fetcher():
    Chairman = leancloud.Object.extend('Chairman')

    def __init__(self):
        self.chairmans = []

    def fetch_douyu(self):
        print 'fetch douyu'

        url = 'http://www.douyu.com/directory/game/How'

        session = requests.Session()
        response = session.get(url, verify=False)

        base_url = 'http://www.douyu.com/'
        # print response.content.decode('utf8')
        for each_content in re.finditer('<a class="play-list-link" .*?>([\s\S]*?)<\/a>', response.content.decode('utf8')):
            try:
                chairman = self.Chairman()
                chairman.type = 'douyu'
                chairman.set('type', 'douyu')

                group = each_content.group()
                # print group
                href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
                chairman.set("href", base_url + href)

                chairman.set("id", chairman.type + str("_") + href.lstrip('/'))

                title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
                chairman.set("title", title)

                img = re.search('data-original=".*?"', group).group().lstrip('data-original="').rstrip('"')
                chairman.set("img", img)

                name = re.search('<span class="dy-name ellipsis fl">.*?</span>', group).group().lstrip('<span class="dy-name ellipsis fl">').rstrip('</span>')
                chairman.set("name", name)

                num = re.search('<span class="dy-num fr.*?</span>', group).group().lstrip('<span class="dy-num fr">').rstrip('</span>')

                if '万' in num:
                    chairman.set("num", int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000)))
                else:
                    chairman.set("num", int(num))

                self.chairmans.append(chairman)
            except Exception, e:
                print group

    def fetch_xiongmao(self):
        print 'fetch xiongmao'

        url = 'http://www.panda.tv/cate/hearthstone'

        session = requests.Session()
        response = session.get(url, verify=False)

        base_url = 'http://www.panda.tv/'
        for each_content in re.finditer('<a href=".*?" class="video-list-item-wrap"([\s\S]*?)<\/a>', response.content.decode('utf8')):
            chairman = self.Chairman()
            chairman.type = 'panda'
            chairman.set('type', 'panda')

            group = each_content.group()
            # print group

            href = re.search('href=".*?"', group).group().lstrip('href="/').rstrip('"')
            chairman.set("href", base_url + href)

            chairman.set("id", chairman.type + str("_") + href.lstrip('/'))

            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            chairman.set("title", title)

            img = re.search('data-original=".*?"', group).group().lstrip('data-original="').rstrip('"')
            chairman.set("img", img)

            if re.search('</i>[\s\S]*?</span>', group):
                name = re.search('</i>[\s\S]*?</span>', group).group().lstrip(
                    '</i>').rstrip('</span>')
                chairman.set("name", name)
            else:
                chairman.set("name", "")

            # print name

            num = re.search('<span class="video-number">.*?</span>', group).group().lstrip(
                '<span class="video-number">').rstrip('</span>')
            num = num.replace('人', '')
            if '万' in num:
                chairman.set("num", int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000)))
            else:
                chairman.set("num", int(num))
            self.chairmans.append(chairman)

    def fetch_quanmin(self):
        print 'fetch quanmin'

        url = 'http://www.quanmin.tv/json/categories/heartstone/list.json?t=24468018'

        session = requests.Session()
        response = session.get(url, verify=False)

        base_url = 'http://www.quanmin.tv/v/'
        for each in response.json()['data']:
            chairman = self.Chairman()
            chairman.type = 'quanmin'
            chairman.set('type', 'quanmin')

            # chairman.objectId = (chairman.type + str("_") + each['uid'])

            # chairman.title = each['title']
            # chairman.href = base_url + each['uid']
            # chairman.img = each['thumb']
            # chairman.name = each['nick']
            # chairman.set_num(str(each['follow']))

            chairman.set("id", (chairman.type + str("_") + each['uid']))
            chairman.set("title", each['title'])
            chairman.set("href", base_url + each['uid'])
            chairman.set("img", each['thumb'])
            chairman.set("name", each['nick'])

            num = str(each['follow'])

            if '万' in num:
                chairman.set("num", int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000)))
            else:
                chairman.set("num", int(num))

            self.chairmans.append(chairman)


    def fetch_zhanqi(self):
        print 'fetch zhangqi'

        url = 'http://www.zhanqi.tv/chns/blizzard/how'

        session = requests.Session()
        response = session.get(url, verify=False)

        base_url = 'http://www.zhanqi.tv/'
        for each_content in re.finditer('<a href=".*?" class="js-jump-link">([\s\S]*?)<\/a>',
                                        response.content.decode('utf8')):
            group = each_content.group()
            href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            if href != '${url}':
                chairman = self.Chairman()
                chairman.type = 'zhanqi'
                chairman.set('type', 'zhanqi')

                # print group

                chairman.set("href", href)

                chairman.set("id", chairman.type + str("_") + href.lstrip('/'))

                title = re.search('<span class="name">.*?</span>', group).group().lstrip('<span class="name">').rstrip('</span>')
                chairman.set("title", title)

                img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
                chairman.set("img", img)

                name = re.search('<span class="anchor anchor-to-cut dv">.*?</span>', group).group().lstrip(
                    '<span class="anchor anchor-to-cut dv">').rstrip('</span>')
                chairman.set("name", name)

                num = re.search('<span class="dv">.*?</span>', group).group().lstrip(
                    '<span class="dv">').rstrip('</span>')
                # chairman.set_num(num)

                if '万' in num:
                    chairman.set("num", int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000)))
                else:
                    chairman.set("num", int(num))

                self.chairmans.append(chairman)

    # def fetch_huomao(self):
    #     url = 'http://www.zhanqi.tv/chns/blizzard/how'
    #
    #     session = requests.Session()
    #     response = session.get(url)
    #
    #     for each_content in re.finditer('<a href=".*?" class="js-jump-link">([\s\S]*?)<\/a>',
    #                                     response.content.decode('utf8')):
    #         chairman = self.Chairman()
    #         group = each_content.group()
    #         # print group
    #
    #         href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
    #         chairman.href = base_url + href
    #
    #         title = re.search('<span class="name">.*?</span>', group).group().lstrip('<span class="name">').rstrip(
    #             '</span>')
    #         chairman.title = title
    #
    #         img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
    #         chairman.img = img
    #
    #         name = re.search('<span class="anchor anchor-to-cut dv">.*?</span>', group).group().lstrip(
    #             '<span class="anchor anchor-to-cut dv">').rstrip('</span>')
    #         chairman.name = name
    #
    #         num = re.search('<span class="dv">.*?</span>', group).group().lstrip(
    #             '<span class="dv">').rstrip('</span>')
    #         chairman.set_num(num)
    #
    #         print chairman

    def fetch_huya(self):
        print 'fetch huya'

        url = 'http://www.huya.com/g/hearthstone'

        session = requests.Session()
        response = session.get(url, verify=False)
        # print response.content
        for each_content in re.finditer('<li class="game-live-item">([\s\S]*?)<\/li>',
                                        response.content.decode('utf8')):
            chairman = self.Chairman()
            chairman.type = 'huya'
            chairman.set('type', 'huya')

            group = each_content.group()
            # print group
            href = re.search('href=".*?"', group).group().lstrip('href=').strip('"')
            chairman.set("href", href)
            chairman.set("id", chairman.type + str("_") + href.lstrip('http://www.huya.com/'))

            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            chairman.set("title", title)
        #
            img = re.search('<img class="pic" data-original=".*?"', group).group().lstrip('<img class="pic" data-original="').rstrip('"')
            # print img
            chairman.set("img", img)

            name = re.search('<i class="nick" title=".*?">', group).group().lstrip(
                '<i class="nick" title="').rstrip('">')
            chairman.set("name", name)

            num = re.search('<i class="js-num">.*?</i>', group).group().lstrip(
                '<i class="js-num">').rstrip('</i>')
            # chairman.set_num(num)
            if '万' in num:
                chairman.set("num", int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000)))
            else:
                chairman.set("num", int(num))

            self.chairmans.append(chairman)

    def fetch_longzhu(self):
        print 'fetch longzhu'

        url = 'http://longzhu.com/channels/hs?from=figame'

        session = requests.Session()
        response = session.get(url, verify=False)
        # print response.content.decode('utf8')
        for each_content in re.finditer('<a href=".*? class="livecard"([\s\S]*?)<\/a>',
                                        response.content.decode('utf8')):
            chairman = self.Chairman()
            chairman.type = 'longzhu'
            chairman.set('type', 'longzhu')

            group = each_content.group()
            # print group

            href = re.search('href=".*?"', group).group().lstrip('href=').strip('"')
            chairman.set("href", href)

            chairman.set("id", (chairman.type + str("_") + href.replace('/', '').lstrip('http://star.longzhu.com/').rstrip('?from=challcontent')))

            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            chairman.set("title", title)

            img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
            chairman.set("img", img)

            name = re.search('<strong class="livecard-modal-username">.*?</strong>', group).group().lstrip(
                '<strong class="livecard-modal-username">').rstrip('</strong>')
            chairman.set("name", name)

            num = re.search('<span class="livecard-meta-item-text">.*?</span>', group).group().lstrip(
                '<span class="livecard-meta-item-text">').rstrip('</span>')

            if '万' in num:
                chairman.set("num", int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000)))
            else:
                chairman.set("num", int(num))

            self.chairmans.append(chairman)

    def fetch_cc(self):
        print 'fetch cc'
        url = 'http://cc.163.com/category/list/?gametype=1005'

        session = requests.Session()
        response = session.get(url, verify=False)

        base_url = 'http://cc.163.com/'

        for each_content in re.finditer('<li class="game-item js-game-item">([\s\S]*?)<\/li>',
                                        response.content.decode('utf8')):
            group = each_content.group()
            href = re.search('href=".*?"', group).group().lstrip('href="/').rstrip('/"')

            if href != '{[value.ccid]}':
                chairman = self.Chairman()
                chairman.type = 'cc'
                chairman.set('type', 'cc')

                # print group

                chairman.set("href", base_url + href)


                # chairman.objectId = (chairman.type + str("_") + href)
                chairman.set("id", (chairman.type + str("_") + href))

                title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
                chairman.set("title", title)

                img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
                chairman.set("img", img)

                name = re.search('<span class="game-item-nick nick" title=".*?">', group).group().lstrip(
                    '<span class="game-item-nick nick" title="').rstrip('">')
                chairman.set("name", name)


                num = re.search('<span class="def-font visitor"></span>([\s\S]*?)</span>', group).group().lstrip(
                    '<span class="def-font visitor"></span>').rstrip('</span>')
                # chairman.set_num(num)

                if '万' in num:
                    chairman.set("num", int(round(float(num.replace('万', '').replace('\r', '').replace('\n', '')) * 10000)))
                else:
                    chairman.set("num", int(num))

                self.chairmans.append(chairman)

if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.fetch_douyu()
    fetcher.fetch_xiongmao()
    fetcher.fetch_quanmin()
    fetcher.fetch_zhanqi()
    # fetcher.fetch_huomao()
    fetcher.fetch_longzhu()
    fetcher.fetch_cc()
    fetcher.fetch_huya()

    # print fetcher.chairmans