import mysql.connector

myconn = mysql.connector.connect(host = "localhost", 
                                 user = "root",
                                 passwd = "abfbh27834",
                                 database = "lab1")
cur = myconn.cursor()

def ERC(command):
    cur.execute(command)
    result = cur.fetchall()
    return result

def EWC(command):
    cur.execute(command)
    cur.commit()
    result = f"{cur.rowcount} Modified."
    return result


myconn.close()