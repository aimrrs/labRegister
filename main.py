import time
from tabulate import tabulate
from dbbro import Dbbro

db = Dbbro()

today_Date = time.strftime("%d,%m,%Y")

class Register:
    def __init__(self):
        pass

    def ifTableExists(self):
        tables = db.ERC("SHOW TABLES")
        for table in tables:
            if today_Date in table:
                return 1
        return 0

    def createTable(self):
        com = f"CREATE TABLE `{today_Date}` (rollno char(120) primary key, sysno int, inorout char(4) not null, intime time not null, outtime time)"
        db.EWC(com)
        return

    def entry(self, rollnumber):
        comand = f"INSERT INTO `{today_Date}` VALUES ({rollnumber}, null, 'IN', CURRENT_TIME, CURRENT_TIME)"
        db.EWC(comand)
        comand = f"SELECT * FROM students WHERE rollno = {rollnumber}"
        det = db.ERC(comand)[0]
        details = f"\nName : {det[0]}\nDepartment : {det[1]}\nYear : {det[2]}\nRoll Number : {det[3]}\nRegister Number : {det[4]}\n"
        return details

    def exitLab(self, rollnumber, sysno):
        command = f"UPDATE `{today_Date}` SET sysno = {sysno}, inorout = 'OUT', outtime = CURRENT_TIME WHERE rollno = '{rollnumber}'"
        b = db.EWC(command)
        return b

    def labCurStat(self):
        allin = db.ERC(f"SELECT * FROM `{today_Date}`")
        for row in range(len(allin)):
            allin[row] = list(allin[row])
            allin[row][-2] = str(allin[row][-2])
            allin[row][-1] = str(allin[row][-1])

        headers = ["Roll Number", "System Number", "In/Out", "In Time", "Out Time"]
        allinTable = tabulate(allin, headers=headers, tablefmt="grid")
        return 