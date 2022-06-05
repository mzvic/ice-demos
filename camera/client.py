import sys, Ice
Ice.loadSlice('camera.ice')
import Demo

def run(communicator):
    twoway = Demo.videoPrx.checkedCast(
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
            if c == 'take photo':
                twoway.take_photo()
            else:
                print("unknown command `" + c + "\'")
                menu()
        except Ice.Exception as ex:
            print(ex)

def menu():
    print("""
usage:
t: take photo
""")


with Ice.initialize(sys.argv, "config.client") as communicator:
    if len(sys.argv) > 1:
        print(sys.argv[0] + ": too many arguments")
        sys.exit(1)
    run(communicator)