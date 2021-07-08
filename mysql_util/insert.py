from mysql_util.pyConnect import get_conn
from datetime import datetime


def insert(sql):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    sql = "insert into stockinfo (name,id, secid) " \
          "values ('%s','%s', '%s')" % ("uuu", "9", datetime.now().strftime("%Y-%m-%d %H:%M:%S"));

    insert(sql)
