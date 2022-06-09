import serial
import sys, os
arduino = serial.Serial('/dev/cu.usbserial-1410', 9600)

def menu():
    print("""
usage:
c: center
r: right
l: left
x: exit
""")

while 1:
    os.system("clear")
    menu()
    command = input("Enter command: ")
    if command == 'l':
        arduino.write('1'.encode())
    elif command == 'c':
        arduino.write('2'.encode())
    elif command == 'r':
        arduino.write('3'.encode())
    elif command == 'x':
        arduino.write('4'.encode())
        quit()
    


