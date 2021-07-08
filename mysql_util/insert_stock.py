from mysql_util.execute import _execute


def create_stock_day_data_table(all_data, stock_name):
    sql = "DROP TABLE IF EXISTS " + stock_name
    _execute(sql)

    sql = "CREATE TABLE `%s` (date date PRIMARY KEY  ,rise_and_fall  varchar (255) , ending_price float )" % (
        stock_name)
    _execute(sql)

    for item in all_data:
        sql = "insert into %s (date ,rise_and_fall , ending_price) " \
              "values ('%s', '%s', '%s')" % (stock_name, item[0], item[2], item[1])
        _execute(sql)


if __name__ == '__main__':
    all_data = [['2021-07-09', '20.4', '-9'], ['2021-07-08', '20.8', '-9']]
    create_stock_day_data_table(all_data, stock_name='ma')
    # sql = "insert into stock (name  ,create_date ,rise_and_fall , ending_price) " \
    #       "values ('%s',' %s', '%s', '%s')" % ("rt2", datetime.now().strftime("%Y-%m-%d") , "-10",10.15);

    # insert(sql)
