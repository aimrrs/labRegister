from main import Register
from time import sleep

rollNumber = input("Enter your roll number : ")

register = Register()

#Create table aka entry for that day.
if not register.ifTableExists():
    register.createTable()

#Entry
out = register.entry(rollNumber)
print(out)

"""
1. To make register, student can only enter their roll no,
    and get their details displayed.
"""