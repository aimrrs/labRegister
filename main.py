import time
from tabulate import tabulate
import mysql.connector

myconn = mysql.connector.connect(host = "localhost", 
                                 user = "root",
                                 passwd = "abfbh27834",
                                 database = "lab1")
cur = myconn.cursor()

today_Date = time.strftime("%d,%m,%Y")

def ERC(command):
    cur.execute(command)
    result = cur.fetchall()
    return result

def EWC(command):
    cur.execute(command)
    myconn.commit()
    result = f"{cur.rowcount} M"
    return result

class Register:
    def __init__(self):
        pass

    def ifTableExists(self):
        tables = ERC("SHOW TABLES")
        for table in tables:
            if today_Date in table:
                return 1
        return 0

    def createTable(self):
        com = f"CREATE TABLE `{today_Date}` (rollno char(120) primary key, sysno int, inorout char(4) not null, intime time not null, outtime time)"
        EWC(com)
        return

    def entry(self, rollnumber):
        comand = f"INSERT INTO `{today_Date}` VALUES ({rollnumber}, null, 'IN', CURRENT_TIME, CURRENT_TIME)"
        a = EWC(comand)
        return a

    def exitLab(self, rollnumber, sysno):
        command = f"UPDATE `{today_Date}` SET sysno = {sysno}, inorout = 'OUT', outtime = CURRENT_TIME WHERE rollno = '{rollnumber}'"
        b = EWC(command)
        return b

    def labCurStat(self):
        allin = ERC(f"SELECT * FROM `{today_Date}`")
        for row in range(len(allin)):
            allin[row] = list(allin[row])
            allin[row][-2] = str(allin[row][-2])
            allin[row][-1] = str(allin[row][-1])

        headers = ["Roll Number", "System Number", "In/Out", "In Time", "Out Time"]
        allinTable = tabulate(allin, headers=headers, tablefmt="grid")
        return allinTable
    

myconn.close()