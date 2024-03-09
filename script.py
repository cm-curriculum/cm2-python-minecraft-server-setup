from mcpi_e.minecraft import Minecraft

serverAddress="147.135.48.77"
pythonApiPort=25565

mc = Minecraft.create(serverAddress, pythonApiPort)

pos = mc.player.getPos()

print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))