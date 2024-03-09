from mcpi_e.minecraft import Minecraft

ip_address = '127.0.0.1'
port = 4711
username = "YOUR_AWESOME_USERNAME"
mc = Minecraft.create('127.0.0.1', 4711, username)

# print the player's position
pos = mc.player.getTilePos()

print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))