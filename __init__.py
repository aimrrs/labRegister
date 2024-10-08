from main import Register
from time import sleep

name = input("Enter your name : ")
nodeNumber = int(input("Enter you place number : "))
rollNumber = int(input("Enter your roll number : "))

register = Register()
register.entry(name, nodeNumber,rollNumber)
sleep(5)
register.exitLab()
sleep(2)
entries = register.inMates()
for entri in entries:
    print(entri)