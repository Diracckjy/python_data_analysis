import pymysql

def get_conn():
    conn = pymysql.connect(host='42.193.38.14', port=3306, user='spiderDemo', passwd='111111', db='spiders')
    return conn