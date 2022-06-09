import os
import serial
from datetime import datetime
import sys, Ice
import signal

arduino = serial.Serial('/dev/cu.usbserial-1410', 9600)
Ice.loadSlice('arduino.ice')
import Demo


class arduinoI(Demo.arduinointerface): #video = interface in camera.ice
    def left(self, current):
        arduino.write('1'.encode())
    def center(self, current):
        arduino.write('2'.encode())
    def right(self, current):
        arduino.write('3'.encode())

    def leftwithtime(self, current):
        print("as")
    def centerwithtime(self, current):
        print("as")
    def rightwithtime(self, current):
        print("as")

    def stop(self, current):
        arduino.write('4'.encode())
        current.adapter.getCommunicator().shutdown()

with Ice.initialize(sys.argv, "config.server") as communicator:
    signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown()) #signal.signal function allows defining custom handlers to be executed when a signal is received

    adapter = communicator.createObjectAdapter("Arduino") #Camera.Proxy (config.client) Camera.Endpoint (config.server)
    adapter.add(arduinoI(), Ice.stringToIdentity("arduino")) #config.client Camera.Proxy=camera:tcp
    adapter.activate()
    communicator.waitForShutdown()