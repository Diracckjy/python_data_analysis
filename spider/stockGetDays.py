import json
import re

import requests


class stockGetDays():
    def __init__(self):
        self.url = 'https://21.push2.eastmoney.com/api/qt/clist/get?pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&pn=1'
        self.url2 = 'https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get?fields1=f1&fields2=f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65&secid='
        self.suburl = 'http://quote.eastmoney.com/kcb/%s.html'

    def run(self):
        urlList = self.parsePage()
        dataList = []
        for i in urlList:
            data = self.subParse(i)
            if data is not None:
                dataList.append(data)
        return self.getData(dataList)

    def getData(self, list):
        ans = []
        for item in list:
            dict = {}
            dict["name"] = item[0]
            dataList = []
            url = self.url2 + str(item[1])
            resp = requests.get(url)
            data = json.loads(resp.text)
            for item in data['data']['klines']:
                dataList.append(item)
            dict["data"] = dataList
            ans.append(dict)
        return ans

    def parsePage(self):
        list = []
        resp = requests.get(self.url)
        resp = json.loads(resp.text)
        for item in resp['data']['diff']:
            url = self.suburl % item['f12']
            list.append(url)
        return list

    def subParse(self, url):
        resp = requests.get(url)
        if resp.status_code == 200:
            resp.encoding = resp.apparent_encoding
            res = re.findall(".*?stockEnity.*?UnifiedId:  '(.*?)'.*?Code: '(.*?)'.*?Name: '(.*?)'", resp.text, re.S)[0]
            secid = res[0]
            name = res[2]
            return name, secid
        else:
            return None


def main():
    spider = stockGetDays()
    a = spider.run()


if __name__ == '__main__':
    main()
