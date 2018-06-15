Linux Service Install (Tested on Ubuntu 12.04)
------------------------------------------------------------------
Requirements:
* Python 2.7           (http://www.python.org/download/)
* psutil 0.6.1         (https://code.google.com/p/psutil/downloads/list)
* Minecraft Server Jar (https://minecraft.net/download)
* Java                 (http://www.oracle.com/technetwork/java/javase/downloads/jre7-downloads-1880261.html)

Install:

Only continue once you have Python 2.7 and psutil 0.6.1 installed.

(Your package manager should ensure everything is the same version, I.E. Java 64bit, Python 64bit, and psutil 64bit or it won't work.)
    
1. Extract the files you've likely downloaded from GitHub into whatever directory you like.
    I'll use /home/chip/butrmanager as our example. This is just a temporary directory.
    
2. CD into the directory and run 'sudo bash install.sh' to begin the install.
    It basically creates /usr/games/butrmanager and moves the core files there and installs butrmanager.conf.
    
3. CD to /usr/games and run 'chown -R USERID butrmanager'.
    This is to make it easier to edit config and server files in future.
    
4. CD to /usr/games/butrmanager and create a directory for your first server instance.
    I use /usr/games/butrmanager/server1 for example.
    
5. Place the relevant minecraft server files into your folder.
    For me that would just be the vanilla minecraft jar, /usr/games/butrmanager/server1/minecraft_server.jar.
    
6. Go back up a directory and modify ServiceConfig.ini with whatever port, hostname, password, and server information you need.
    The INI has fairly detailed comments on what each section does and how to configure them.
    
7. Once you've ran the install script, added your instance files, and edited ServiceConfig.ini you're ready to start the service.
    It can be started with 'sudo start butrmanager' and will create /usr/games/butrmanager/butrmanager.log.
    
Note:
    Service can be stopped via 'sudo stop butrmanager'
    Uninstalling the service is as simple as removing /etc/init/butrmanager.conf and reloading init control.
    Feel free to email admin@butrcraft.com with any issues you experience, still very much an in dev kinda thing here.
