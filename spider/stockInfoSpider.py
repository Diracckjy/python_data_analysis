import json

import pymysql
import requests

# 当虹科技
class stockInfoSpier():
    def __init__(self, name):
        self.name = name
        self.url = 'https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?fields1=f1&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65&secid='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

    def run(self):
        secid = self.getSecid(self.name)
        if secid is None:
            print('没有该公司数据')
        else:
            print('该公司secid为：' + str(secid[0]))
            self.parse(secid[0])

    def parse(self, secid):
        self.url = self.url + str(secid)
        print(self.url)
        resp = requests.get(self.url, headers=self.headers)
        if resp.status_code == 200:
            items = json.loads(resp.text)
            for item in items['data']['klines']:
                print(item)

    def getSecid(self, name):
        conn = pymysql.connect(host='42.193.38.14', port=3306, user='spiderDemo', passwd='111111', db='spiders')
        cur = conn.cursor()
        sql = 'SELECT secid FROM stockinfo WHERE name = %s'
        cur.execute(sql, (name))
        result = cur.fetchone()
        return result


def main():
    name = input("请输入要爬取的公司名称：")
    spider = stockInfoSpier(name)
    spider.run()


if __name__ == '__main__':
    main()
