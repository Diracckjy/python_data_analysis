import pymysql


class stockInfoSpier():
    def __init__(self, name):
        self.name = name

    def run(self):
        secid = self.getSecid(self.name)

    def getSecid(self, name):
        conn = pymysql.connect(host='42.193.38.14', port=3306, user='spiderDemo', passwd='111111', db='spiders')
        cur = conn.cursor()
        sql = 'SELECT secid FROM stockinfo WHERE name = %s'
        cur.execute(sql, (name))
        result = cur.fetchone()
        if result is None:
            print('没有该公司数据')
        else:
            print('该公司secid为：' + str(result[0]))


def main():
    name = input("请输入要爬取的公司名称：")
    spider = stockInfoSpier(name)
    spider.run()


if __name__ == '__main__':
    main()
