import sys, Ice
import test
 
with Ice.initialize(sys.argv) as communicator:
    base = communicator.stringToProxy("SimplePrinter:default -p 10000")
    printer = test.printerPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy")
 
    printer.printstring("Jelou")
