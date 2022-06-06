import sys, Ice
from datetime import datetime
Ice.loadSlice('camera.ice')
import Demo

def run(communicator):
    twoway = Demo.videoPrx.checkedCast( #videoPrx = interfacePrx (interface proxy)
        communicator.propertyToProxy('Camera.Proxy').ice_twoway().ice_secure(False))
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
            if c == 't':
                twoway.takephoto()
            elif c == 's':
                twoway.shutdown()
            elif c == 'x':
                pass
            else:
                print("unknown command `" + c + "\'")
                menu()
        except Ice.Exception as ex:
            print(ex)

def menu():
    print("""
usage:
t: take photo
s: shutdown server
x: exit
""")


with Ice.initialize(sys.argv, "config.client") as communicator:
    run(communicator)