import pymysql
#连接数据库
def get_conn():
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',db='test')
    return conn

def create_stock_table(sql):
    conn = get_conn()
    cur = conn.cursor()
    result = cur.execute(sql)
    print(result)
    conn.commit() #提交事务
    cur.close()
    conn.close()

if __name__ == '__main__':
    sql = "CREATE TABLE stock (name varchar(255) PRIMARY KEY  ,create_date date  ,rise_and_fall  varchar (255) , ending_price float )" ;

    create_stock_table(sql)
