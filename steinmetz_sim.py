import pybullet as p
import time
import math
import pybullet_data


physicsClient = p.connect(p.GUI) # or p.DIRECT for non-graphical version

p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally

p.setGravity(0,0,-10)

p.resetDebugVisualizerCamera(cameraDistance=1, cameraYaw=30, cameraPitch=-30, cameraTargetPosition=[0, 0, 0.5])


planeId = p.loadURDF("models/plane.urdf")

startPos = [0,0,0.30]
startOrientation = p.getQuaternionFromEuler([0,math.radians(90),0])
sphereId = p.loadURDF("models/cylinder.urdf",startPos, startOrientation)

#                                  force       position    or LINK_FRAME
p.applyExternalForce(sphereId, -1, [0, 20, 0], [0,0,0.3], p.WORLD_FRAME)

while True:
    try:
        p.stepSimulation()
        time.sleep(1./1000.)
    except:
        raise
p.disconnect()
