import mysql.connector

myconn = mysql.connector.connect(host = "localhost", 
                                 user = "root",
                                 passwd = "abfbh27834",
                                 database = "lab1")
cur = myconn.cursor()







myconn.close()