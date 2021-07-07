import pymysql

def get_conn():
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='test')
    return conn