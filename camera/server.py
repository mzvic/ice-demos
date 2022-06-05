import sys, Ice
import signal
import pygame
import pygame.camera

Ice.loadSlice('camera.ice')
import Demo

class cameraI(Demo.video): #video = interface in camera.ice
    def takephoto(self, current):
        pygame.camera.init()
        pygame.camera.list_cameras() #Camera detected or not
        cam = pygame.camera.Camera("FaceTime HD Camera",(640,480))
        cam.start()
        img = cam.get_image()
        pygame.image.save(img,"filename.jpg")

    def shutdown(self, current):
        current.adapter.getCommunicator().shutdown()

with Ice.initialize(sys.argv, "config.server") as communicator:
    signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown())

    if len(sys.argv) > 1:
        print(sys.argv[0] + ": too many arguments")
        sys.exit(1)

    adapter = communicator.createObjectAdapter("Camera")
    adapter.add(cameraI(), Ice.stringToIdentity("camera"))
    adapter.activate()
    communicator.waitForShutdown()



