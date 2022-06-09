import sys, Ice
from datetime import datetime
Ice.loadSlice('arduino.ice')
import Demo

def run(communicator):
    twoway = Demo.arduinointerfacePrx.checkedCast( #nterfacePrx (interface proxy)
        communicator.propertyToProxy('Arduino.Proxy').ice_twoway().ice_secure(False))
    if not twoway:
        print("invalid proxy")
        sys.exit(1)

    menu()
    c = None
    while c!= 'x':
        try: 
            sys.stdout.write("==>")
            sys.stdout.flush()
            c = sys.stdin.readline().strip()
            if c == 'c':
                twoway.center()
            elif c == 'r':
                twoway.right()
            elif c == 'l':
                twoway.left()
            elif c == 'x':
                twoway.stop()
            else:
                print("unknown command `" + c + "\'")
                menu()
        except Ice.Exception as ex:
            print(ex)

def menu():
    print("""
usage:
c: center
r: right
l: left
x: exit
""")
with Ice.initialize(sys.argv, "config.client") as communicator:
    run(communicator)