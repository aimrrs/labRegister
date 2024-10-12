import mysql.connector

class Dbbro:
    def __init__ (self):
        self.myconn = mysql.connector.connect(host = "localhost", 
                                    user = "root",
                                    passwd = "abfbh27834",
                                    database = "lab1")
        
        self.cur = self.myconn.cursor()

    def ERC(self, command):
        self.cur.execute(command)
        result = self.cur.fetchall()
        return result

    def EWC(self, command):
        self.cur.execute(command)
        self.myconn.commit()
        result = f"{self.cur.rowcount} M"
        return result

    def closeDbbro(self):
        self.cur.close()
        self.myconn.close()