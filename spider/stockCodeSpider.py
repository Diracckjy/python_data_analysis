import json
import re
import pymysql

import requests
from tqdm import tqdm


class stockCodeSpider():
    def __init__(self):
        self.url = 'https://21.push2.eastmoney.com/api/qt/clist/get?pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&pn='
        self.rec = 0
        self.suburl = 'http://quote.eastmoney.com/kcb/%s.html'
        self.conn = None

    def run(self):
        self.conn = pymysql.connect(user='spiderDemo', password='111111', host='42.193.38.14', database='spiders',
                                    port=3306,
                                    charset='utf8')
        list = self.parseMainPage()
        dataList = []
        for i in tqdm(list):
            data = self.subParse(i)
            if data is not None:
                dataList.append(data)
            if len(dataList) == 100:
                self.saveToDB(dataList)
                dataList = []
        self.saveToDB(dataList)
        self.conn.close()

    def parseMainPage(self):
        list = []
        for i in range(1, 17):
            resp = requests.get(self.url + str(i))
            resp = json.loads(resp.text)
            for item in resp['data']['diff']:
                url = self.suburl % item['f12']
                list.append(url)
        return list

    def subParse(self, url):
        resp = requests.get(url)
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            res = re.findall(".*?stockEnity.*?UnifiedId:  '(.*?)'.*?Name: '(.*?)'", resp.text, re.S)[0]
            name = res[1]
            secid = res[0]
            self.rec = self.rec + 1
            return str(self.rec), name, secid
        else:
            return None

    def saveToDB(self, list):
        cur = self.conn.cursor()
        for data in list:
            sql = 'INSERT INTO spiders.stockinfo(id, name, secid) VALUES(%s, %s, %s)'
            cur.execute(sql, data)
        self.conn.commit()
        cur.close()


def main():
    spider = stockCodeSpider()
    spider.run()


if __name__ == '__main__':
    main()
