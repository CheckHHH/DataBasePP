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

