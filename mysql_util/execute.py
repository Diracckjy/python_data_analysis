from mysql_util.pyConnect import get_conn

def _execute(sql):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit() #提交事务
    cur.close()
    conn.close()