from os import path
import time

class Register:
    def __init__(self):
        self.currentTime = time.strftime("%H:%M:%S")
        self.todayDate = time.strftime("%Y-%m-%d")
        self.inCount = 0
        self.outCount = 0
        self.name = None
        self.nodeNumber = None
        self.rollNumber = None

    def entry(self, name, nodeNumber, rollNumber):
        self.name, self.nodeNumber, self.rollNumber = name, nodeNumber, rollNumber

        if path.exists(f"{self.todayDate}.txt"):
            with open(f"{self.todayDate}.txt", "a+") as entryFileObject:
                entryFileObject.write(f"{name} : {nodeNumber} : {rollNumber} : IN - {self.currentTime} : OUT - (not yet)\n")
        else:
            with open(f"{self.todayDate}.txt", "w") as fotemp:
                pass

        self.inCount += 1
        return

    def exitLab(self):
        if path.exists(f"{self.todayDate}.txt"):
            with open(f"{self.todayDate}.txt", "a+") as ELFileObject:
                ELFileObject.write(f"{self.name} : {self.nodeNumber} : {self.rollNumber} : IN - {self.currentTime} : OUT - {self.currentTime}\n")
        else:
            with open(f"{self.todayDate}.txt", "w") as fotemp:
                pass

        self.outCount += 1
        return

    def inMates(self):
        inMatesList = []
        if path.exists(f"{self.todayDate}.txt"):
            with open(f"{self.todayDate}.txt", "r") as inMatesFileObject:
                if (len(inMatesFileObject.readlines()) != 0) and (self.inCount - self.outCount != 0):
                    entries = inMatesFileObject.readlines()
                    for entri in entries:
                        if ": IN - " in entri:
                            inMatesList.append(entri)
        return inMatesList