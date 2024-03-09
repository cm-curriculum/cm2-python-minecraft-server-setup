# Introduction

This repository is a modification of the repository as provided in the book [*Learn to Program with Minecraft*](https://drive.google.com/file/d/1EQVwgLZEhAXqAstCfXrSISIlRx0LWe6_/view) by Craig Richardson. Specifically, the instructions loosely follow that as that of Chapter 1, but with modifications as the Python project from the book is outdated.

## Instructions

### Getting Minecraft

If you don't already have Minecraft, then follow these steps.

1. Purchase Minecraft. You will need an account with a password.
2. Go to [https://minecraft.net/download](https://minecraft.net/download). From here you will install the Minecraft launcher.
3. Open the Minecraft Launcher, and then log into your Minecraft account.
4. Install Minecraft version 1.16.3.

### Installing Python

You will need Python in order to make programs.

1. Go to [http://www.python.org/downloads/](http://www.python.org/downloads/). From here you will install the newest version of Python.
2. Once the installer has downloaded, run it.
3. For Windows users, when the installer opens, select "Add Python to Path".
4. A dialog might ask if you want to install additional software on your computer. Click "Yes."

### Installing Java

Java is required for you to run your Minecraft server. We will use a specialized program named Spigot to run the Minecraft server.

5. Install a [JDK](https://www.oracle.com/java/technologies/downloads/#jdk21-windows) depending on your system (Mac or Windows).
6. For Windows users, make sure that Java was added to your path. To test this, you can open up a terminal and run "java --version", and if you don't get an error you're good to go.
   
### Running the Server

6. Install the project by pulling it from Github onto a local machine or by installing it as a .zip file and unzipping it.
7. Double click on "Install_API.bat". This will open a terminal window to install all the necessary Python libraries.
8. Double click on "Start_Server.lnk". This will start up the Minecraft server on Spigot. It may take a minute or two. A terminal window will pop up and you will know that it's ready once the terminal prompts you to enter a command or use "/help".
9. Open up Minecraft version 1.16.3. 
10. Go to the "Multiplayer" tab.
11. Click on the "Add Server" button.
12. Call the server whatever you want. In the field that says "Server Address," type in "localhost". Then click "Done."
13. Join the server.

### Coding

Whenever you are coding in Python Minecraft you will need 3 things open:

1. The Minecraft server
2. Your Minecraft character in the server itself.
3. A local Python IDE

For a local Python IDE, you can get something like VSCode or you can use IDLE, which actually comes with Python.

The included script.py file in this repository contains a piece of starter code that you can use to test that your installation worked. If you need it, here's what it says:

```python
from mcpi_e.minecraft import Minecraft

mc = Minecraft.create()

# print the player's position
pos = mc.player.getPos()
print("pos: x:{},y:{},z:{}".format(pos.x,pos.y,pos.z))
```