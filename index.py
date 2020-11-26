import os

printing = input("What would you like to print?")
command = './print.sh ' + printing
os.system(command)