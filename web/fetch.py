# -*- coding:utf-8 -*-

import json
import re
import requests

from web.chairman import Chairman

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Fetcher():
    def fetch_douyu(self):
        url = 'http://www.douyu.com/directory/game/How'

        session = requests.Session()
        response = session.get(url)

        base_url = 'http://www.douyu.com/'

        for each_content in re.finditer('<a href=".*?" title=".*?"  >([\s\S]*?)<\/a>', response.content.decode('utf8')):
            chairman = Chairman()
            group = each_content.group()
            # print group
            href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            chairman.href = base_url + href

            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            chairman.title = title

            img = re.search('data-original=".*?"', group).group().lstrip('data-original="').rstrip('"')
            chairman.img = img

            name = re.search('<span class="dy-name ellipsis fl">.*?</span>', group).group().lstrip('<span class="dy-name ellipsis fl">').rstrip('</span>')
            chairman.name = name

            num = re.search('<span class="dy-num fr">.*?</span>', group).group().lstrip('<span class="dy-num fr">').rstrip('</span>')
            chairman.num = num

            print chairman

    def fetch_xiongmao(self):
        url = 'http://www.panda.tv/cate/hearthstone'

        session = requests.Session()
        response = session.get(url)

        base_url = 'http://www.panda.tv/'

        for each_content in re.finditer('<a href=".*?" class="video-list-item-wrap"([\s\S]*?)<\/a>', response.content.decode('utf8')):
            chairman = Chairman()
            group = each_content.group()
            # print group

            href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            chairman.href = base_url + href

            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            chairman.title = title

            img = re.search('data-original=".*?"', group).group().lstrip('data-original="').rstrip('"')
            chairman.img = img

            name = re.search('<span class="video-nickname">.*?</span>', group).group().lstrip(
                '<span class="video-nickname">').rstrip('</span>')
            chairman.name = name

            num = re.search('<span class="video-number">.*?</span>', group).group().lstrip(
                '<span class="video-number">').rstrip('</span>')
            chairman.num = num

            print chairman

    def fetch_quanmin(self):
        url = 'http://www.quanmin.tv/json/categories/heartstone/list.json?t=24468018'

        session = requests.Session()
        response = session.get(url)

        for each in response.json()['data']:
            chairman = Chairman()
            print each


    def fetch_zhanqi(self):
        url = 'http://www.zhanqi.tv/chns/blizzard/how'

        session = requests.Session()
        response = session.get(url)

        base_url = 'http://www.zhanqi.tv/'

        for each_content in re.finditer('<a href=".*?" class="js-jump-link">([\s\S]*?)<\/a>',
                                        response.content.decode('utf8')):
            chairman = Chairman()
            group = each_content.group()
            # print group

            href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            chairman.href = base_url + href

            title = re.search('<span class="name">.*?</span>', group).group().lstrip('<span class="name">').rstrip('</span>')
            chairman.title = title

            img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
            chairman.img = img

            name = re.search('<span class="anchor anchor-to-cut dv">.*?</span>', group).group().lstrip(
                '<span class="anchor anchor-to-cut dv">').rstrip('</span>')
            chairman.name = name

            num = re.search('<span class="dv">.*?</span>', group).group().lstrip(
                '<span class="dv">').rstrip('</span>')
            chairman.num = num

            print chairman

    # def fetch_huomao(self):
    #     url = 'http://www.zhanqi.tv/chns/blizzard/how'
    #
    #     session = requests.Session()
    #     response = session.get(url)
    #
    #     for each_content in re.finditer('<a href=".*?" class="js-jump-link">([\s\S]*?)<\/a>',
    #                                     response.content.decode('utf8')):
    #         chairman = Chairman()
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
    #         chairman.num = num
    #
    #         print chairman

    def fetch_longzhu(self):
        url = 'http://longzhu.com/channels/hs?from=figame'

        session = requests.Session()
        response = session.get(url)

        for each_content in re.finditer('<a href=".*? class="livecard"([\s\S]*?)<\/a>',
                                        response.content.decode('utf8')):
            chairman = Chairman()
            group = each_content.group()
            print group

            href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            chairman.href = href

            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            chairman.title = title

            img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
            chairman.img = img

            name = re.search('<strong class="livecard-modal-username">.*?</strong>', group).group().lstrip(
                '<strong class="livecard-modal-username">').rstrip('</strong>')
            chairman.name = name

            num = re.search('<span class="livecard-meta-item-text">.*?</span>', group).group().lstrip(
                '<span class="livecard-meta-item-text">').rstrip('</span>')
            chairman.num = num

            print chairman

    def fetch_cc(self):
        url = 'http://cc.163.com/category/list/?gametype=1005'

        session = requests.Session()
        response = session.get(url)

        base_url = 'http://cc.163.com/'

        for each_content in re.finditer('<li class="game-item js-game-item">([\s\S]*?)<\/li>',
                                        response.content.decode('utf8')):
            chairman = Chairman()
            group = each_content.group()
            print group

            href = re.search('href=".*?"', group).group().lstrip('href="').rstrip('"')
            chairman.href = base_url + href

            title = re.search('title=".*?"', group).group().lstrip('title="').rstrip('"')
            chairman.title = title

            img = re.search('<img src=".*?"', group).group().lstrip('<img src="').rstrip('"')
            chairman.img = img

            name = re.search('<span class="game-item-nick nick" title=".*?">', group).group().lstrip(
                '<span class="game-item-nick nick" title="').rstrip('">')
            chairman.name = name

            # num = re.search('<span class="def-font visitor"></span>.*?</span>', group).group().lstrip(
            #     '<span class="def-font visitor"></span>').rstrip('</span>')
            # chairman.num = num

            print chairman

if __name__=="__main__":
    fetcher = Fetcher()
    # fetcher.fetch_douyu()
    # fetcher.fetch_xiongmao()
    # fetcher.fetch_quanmin()
    # fetcher.fetch_zhanqi()
    # fetcher.fetch_huomao()
    # fetcher.fetch_longzhu()
    fetcher.fetch_cc()