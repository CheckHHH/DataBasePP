import pymysql
import sys
import re

class DataBaseApi:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        try:
            with self.connection:
                self.cr = self.connection.cursor()
                self.cr.execute("SELECT VERSION()")
                print(self.connection.get_host_info())
        except:
            sys.exit()

    def registration(self, FIO, number, email, datebrith):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `clients` (`FIO`,`phone`, `email`, `datebrith`) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (FIO, number, email, datebrith))
            self.connection.commit()

    def new_service(self, client_id, info, date, stat, summ):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO `orders` (`client_id`, `stat`, `date_acceptance`, `info`, `summ`) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (client_id, stat, date, info, summ))
            self.connection.commit()

    def show_all_service(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''select orders.order_id, clients.FIO, orders.stat, orders.date_acceptance from orders
            JOIN clients ON orders.client_id = clients.id
            '''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print(123)
            return result

    def showOrderDialog(self, num):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''SELECT clients.FIO, orders.date_acceptance, orders.info, orders.summ 
                    FROM orders 
                    JOIN clients ON orders.client_id = clients.id
                    WHERE orders.order_id = {num};
            '''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print(123)
            return result
