import pymysql

def get_conn():
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='test')
    return conn

def update(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql,args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    sql = 'UPDATE  kg_python_user SET value=%s WHERE id = %s;'
    args = ('15', 2)
    update(sql, args)