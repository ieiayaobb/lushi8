import re
import requests


class Fetcher():
    def fetch_douyu(self):
        url = 'http://www.douyu.com/directory/game/How'

        session = requests.Session()
        response = session.get(url)

        for each_content in re.finditer('<a href=".*?" title=".*?"  >([\s\S]*?)<\/a>', response.content.decode('utf8')):
            print each_content.group()
            # topic_title = re.search('id="">.*?</a>', each_content.group()).group().lstrip('id="">').rstrip('</a>')

    def fetch_xiongmao(self):
        url = 'http://www.panda.tv/cate/hearthstone'

        session = requests.Session()
        response = session.get(url)

        for each_content in re.finditer('<a href=".*?" class="video-list-item-wrap"([\s\S]*?)<\/a>', response.content.decode('utf8')):
            print each_content.group()
            # topic_title = re.search('id="">.*?</a>', each_content.group()).group().lstrip('id="">').rstrip('</a>')

    def fetch_quanmin(self):
        url = 'http://www.quanmin.tv/json/categories/heartstone/list.json?t=24468018'

        session = requests.Session()
        response = session.get(url)

        print response.content.decode('utf8')

    def fetch_zhanqi(self):
        url = 'http://www.zhanqi.tv/chns/blizzard/how'

        session = requests.Session()
        response = session.get(url)

        print response.content.decode('utf8')

    def fetch_huomao(self):
        url = 'http://www.zhanqi.tv/chns/blizzard/how'

        session = requests.Session()
        response = session.get(url)

        print response.content.decode('utf8')

    def fetch_longzhu(self):
        url = 'http://longzhu.com/channels/hs?from=figame'

        session = requests.Session()
        response = session.get(url)

        print response.content.decode('utf8')

    def fetch_cc(self):
        url = 'http://cc.163.com/category/list/?gametype=1005'

        session = requests.Session()
        response = session.get(url)

        print response.content.decode('utf8')

if __name__=="__main__":
    fetcher = Fetcher()
    # fetcher.fetch_douyu()
    # fetcher.fetch_xiongmao()
    fetcher.fetch_quanmin()
    # fetcher.fetch_zhanqi()
    # fetcher.fetch_huomao()
    # fetcher.fetch_longzhu()
    # fetcher.fetch_cc()