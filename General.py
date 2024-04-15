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
            log = f'''SELECT orders.order_id, clients.FIO, orders.stat, orders.date_acceptance FROM orders
            JOIN clients ON orders.client_id = clients.id
            '''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print(123)
            return result

    def show_all_clients(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''SELECT * FROM clients'''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print(321)
            return result

    def showOrderDialog(self, num):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''SELECT clients.FIO, orders.date_acceptance, orders.info, orders.summ, orders.stat
                    FROM orders 
                    JOIN clients ON orders.client_id = clients.id
                    WHERE orders.order_id = {num};
            '''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print(123)
            return result

    def showClientDialog(self, num):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''SELECT clients.FIO, clients.phone, clients.email, clients.datebrith
                    FROM clients 
                    WHERE clients.id = {num};
            '''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print(123)
            return result

    def findOrders(self, str):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''SELECT orders.order_id, clients.FIO, orders.stat, orders.date_acceptance FROM orders
                        JOIN clients ON orders.client_id = clients.id
                        WHERE order_id LIKE '%{str}%' OR 
                        clients.FIO LIKE '%{str}%' OR
                        date_acceptance LIKE '%{str}%';
                    '''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print()
            return result

    def findClients(self, str):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''SELECT * FROM clients
                        WHERE FIO LIKE '%{str}%' OR 
                        phone LIKE '%{str}%' OR
                        email LIKE '%{str}%' OR
                        datebrith LIKE '%{str}%';
                            '''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print()
            return result

    def deleteClient(self, client_id):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            with self.connection.cursor() as cursor:
                sql_1 = '''DELETE orders
                           FROM orders
                            JOIN clients ON orders.client_id = clients.id
                            WHERE client_id = %s;'''
                sql_2 = "DELETE FROM clients WHERE id = %s"
                cursor.execute(sql_1, (client_id))
                cursor.execute(sql_2, (client_id))
            self.connection.commit()

    def changeClient(self, FIO, num, email, date, client_id):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "UPDATE clients SET FIO = %s, phone = %s, email = %s, datebrith = %s WHERE id = %s"
                cursor.execute(sql, (FIO, num, email, date, client_id))
            self.connection.commit()

    def listClient(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            self.cr = self.connection.cursor()
            log = f'''SELECT clients.FIO, clients.id FROM clients'''
            self.cr.execute(log)
            result = self.cr.fetchall()
            for x in result:
                print(123)
            return result

    def deleteOrder(self, client_id):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = '''DELETE FROM orders WHERE order_id = %s'''
                cursor.execute(sql, (client_id))
            self.connection.commit()

    def completeOrder(self, row, stat):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='admin',
                                          database='bd')
        with self.connection:
            with self.connection.cursor() as cursor:
                sql = "UPDATE orders SET stat = %s WHERE order_id = %s"
                cursor.execute(sql, (stat, row,))
            self.connection.commit()