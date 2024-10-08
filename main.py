import time

class Register:
    def __init__(self):
        self.currentTime = time.strftime("%H : %M : %S")
        self.todayDate = time.strftime("%Y / %m / %d")
        self.inCount = 0
        self.outCount = 0
        self.name = None
        self.placeNumber = None
        self.rollNumber = None
        self.fileObject = open(f"{self.todayDate}.txt", "a")


    def entry(self, name, placeNumber, rollNumber):
        self.name, self.placeNumber, self.rollNumber = name, placeNumber, rollNumber
        self.fileObject.writeline(f"{name} : {placeNumber} : {rollNumber} : IN - {self.currentTime}")
        inCount += 1
        return

    def exitLab(self):
        self.fileObject.writeline(f"{self.name} : {self.placeNumber} : {self.rollNumber} : IN - {self.currentTime} : OUT - {self.currentTime}")
        outCount += 1
        return

    def inMates(self):
        inMatesList = []
        if (len(self.fileObject.readlines()) != 0) and (self.inCount - self.outCount != 0):
            entries = self.fileObject.readlines()
            for entri in entries:
                if ": IN - " in entri:
                    inMatesList.append(entri)
        return inMatesList