import pymysql

def get_conn():
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='test')
    return conn

def delete(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql,args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    sql = 'DELETE FROM kg_python_user WHERE id = %s;'
    args = (1,) # 单个元素的tuple写法
    delete(sql,args)