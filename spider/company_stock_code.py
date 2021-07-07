import re
import pymysql

import requests
from lxml import etree
from tqdm import tqdm


class stockCodeSpider():
    def __init__(self):
        self.url = 'http://quote.eastmoney.com/usstocklist.html'
        self.rec = 0

    def run(self):
        self.parseMainPage()

    def parseMainPage(self):
        resp = requests.get(self.url)
        resp.encoding = resp.apparent_encoding
        html = etree.HTML(resp.text)
        urlLists = html.xpath('//div[@id="quotesearch"]/ul/li/a/@href')
        print(len(urlLists))
        list = []
        cnt = 1
        for url in tqdm(urlLists):
            data = self.subParse(url)
            if data is not None:
                list.append(data)

            if cnt % 200 == 0:
                self.saveToDB(list)
                print('checkpoint!')
                list = []
            cnt = cnt + 1
            # time.sleep(0.1)
        self.saveToDB(list)

    def subParse(self, url):
        resp = requests.get(url)
        resp.encoding = resp.apparent_encoding
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            name = re.findall('.*?quote_title_0 wryh">(.*?)</span>', resp.text)[0]
            secid = re.findall('.*?stockEnity.*?UnifiedID:"(.*?)"', resp.text, re.S)[0]
            self.rec = self.rec + 1
            return str(self.rec), name, secid
        else:
            return None

    def saveToDB(self, list):
        conn = pymysql.connect(user='root', password='raymond', host='localhost', database='spiders', port=3306,
                               charset='utf8')
        cur = conn.cursor()
        for data in list:
            sql = 'INSERT INTO spiders.stockinfo(id, name, secid) VALUES(%s, %s, %s)'
            cur.execute(sql, data)
        conn.commit()
        cur.close()
        conn.close()


def main():
    spider = stockCodeSpider()
    spider.run()


if __name__ == '__main__':
    main()
