from connect import get_conn

def renew(sql,args):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql,args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    sql = 'UPDATE  stockinfo SET name=%s WHERE id = %s;'
    args = ('150', 1)
    renew(sql, args)