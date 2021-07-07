import pymysql

def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='test')
    return conn

def search(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql,args)
    results = cur.fetchall()
    print(type(results))  # 返回<class 'tuple'> tuple元组类型

    for row in results:
        id = row[0]
        name = row[1]
        value = row[2]
        create_date = row[3]

        print('id:' + str(id) + ' name:' + name + '  value: ' + value + '  create_date: ' + str(create_date))
        pass

    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    sql = 'SELECT  * FROM kg_python_user;'
    search(sql,None)