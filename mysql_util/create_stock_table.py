from mysql_util.execute import _execute
#连接数据库

if __name__ == '__main__':
    sql = "CREATE TABLE stock (name varchar(255) PRIMARY KEY  ,create_date date  ,rise_and_fall  varchar (255) , ending_price float )"
    _execute(sql)
