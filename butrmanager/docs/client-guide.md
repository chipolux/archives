Windows/*Nix Client Install/Info
==================================================================

Description
------------------------------------------------------------------
It's possible to use Client.py either as a command line utility by supplying arguments or as an interface. 
(Much like Diskpart on Windows which is what I based much of my design off of.)

Install
------------------------------------------------------------------
Requirements:
* Python 2.7         (http://www.python.org/download/)

Install:
    
1. Extract the files you've likely downloaded from GitHub into whatever directory you like.
    
2. Open ClientConfig.ini and adjust accordingly. Details are commented into the INI.
    
3. That's pretty much it. The client requires very little setup.
    
Note:
    Client.py only requires Python 2.7 and for ClientConfig.ini to be in the same directory. Simple as that.
    Feel free to email admin@butrcraft.com with any issues you experience, still very much an in dev kinda thing here.

Command Line Usage
------------------------------------------------------------------
Available Command Line Arguments:
* -Server
* -Instance
* -CommandType
* -Command

Each argument is case sensitive but the values supplied can be cased in whatever method you like.
Available values for each argument are as follows.

-Server
* Any server section specified in ClientConfig.ini. 

-Instance
* Any instance name, -Server has to be specified. If -Server not specified it will use the Local.

-CommandType
* All commands require -Server, if not specified it will use Local.
* List, lists all available instances on the specified server.
* Online, lists all online instances on the specified server.
* Exit, will attempt to shutdown the specified server.
* Start, will attempt to start the specified instance. Requires -Instance.
* Stop, will attempt to stop the specified instance. Requires -Instance.
* Command, will attempt to send a command to the specified instance. Requires -Instance and -Command.

-Command
* Only used when -Instance and -CommandType Command is used.
* Needs a string to send to the specified instance as a minecraft server command. If there are spaces in the command quotes are required.
* Example: -Command toggledownfall or -Command 'msg chipolux Hey there!'

Interface Usage
------------------------------------------------------------------
Interface usage is arguably much simpler than command line. Though command line usage provides one line of easily
parsable output and as such is best for scripting which was a major motivator behind desiging and building this.

To access the interface simply run Client.py either from command line with 'python Client.py' or by double clicking
on it in most windowed interfaces.

To find the usage for most commands simply use HELP, it should provide an adequate description of whats available and how to use it.

Important Note
------------------------------------------------------------------
The ability to send commands into the server instance was added mostly as a way to quickly test functionality.
It is NOT recommended as the main way to interface with the server. Instead I would highly reccomend that you
use the built in RCON functionality which is much more standard and secure and is the way I interface
with my production servers to send commands etc.

This utility is mostly meant to aid in automatically starting and stopping remote minecraft servers while
requiring very little overhead and being highly expandable. Not much else.
