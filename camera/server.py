import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from datetime import datetime
import sys, Ice
import signal
import pygame
import pygame.camera

Ice.loadSlice('camera.ice')
import Demo


class cameraI(Demo.video): #video = interface in camera.ice
    def takephoto(self, current):
        pygame.camera.init()
        print(pygame.camera.list_cameras()) #Camera detected or not
        cam = pygame.camera.Camera("FaceTime HD Camera",(1280,720)) #Camera name = FaceTime HD Camera, resolution = 640x480
        cam.start()
        img = cam.get_image()
        pygame.image.save(cam.get_image(),f"{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}.jpg")

    def shutdown(self, current):
        current.adapter.getCommunicator().shutdown()

with Ice.initialize(sys.argv, "config.server") as communicator:
    signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown()) #signal.signal function allows defining custom handlers to be executed when a signal is received

    adapter = communicator.createObjectAdapter("Camera") #Camera.Proxy (config.client) Camera.Endpoint (config.server)
    adapter.add(cameraI(), Ice.stringToIdentity("camera")) #config.client Camera.Proxy=camera:tcp
    adapter.activate()
    communicator.waitForShutdown()



