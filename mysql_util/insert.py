from datetime import datetime
from mysql_util.execute import _execute

if __name__ == '__main__':
    sql = "insert into stockinfo (name,id, secid) " \
          "values ('%s','%s', '%s')" % ("uuu", "9", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    _execute(sql)
