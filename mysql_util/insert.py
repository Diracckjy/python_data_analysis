import pymysql
from datetime import datetime;

def get_conn():
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='test')
    return conn

def insert(sql):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql)
    print(result)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    sql = "insert into kg_python_user (name,value, create_date) " \
          "values ('%s','%s', '%s')" % ("uuu", "9", datetime.now().strftime("%Y-%m-%d %H:%M:%S"));

    insert(sql)
