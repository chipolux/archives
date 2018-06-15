# -*- coding: utf-8 -*-
"""
TextAdv1
Basic text adventure game for fun.

Created on Mon Sep 10 19:25:56 2012

@author: chipolux
"""
import GameLocations as GLoc
import GameEntities as GEnt
import GamePlayer as GPlay
import colorama as CL
import random
import os
import re

# Initialize Colorama
CL.init(autoreset=True)

# Define help message
helpMessage = CL.Fore.YELLOW + CL.Style.BRIGHT + """Accepted Commands:
    Get {ITEM}      Searches for item in area and picks it up if possible.
    Examine {ITEM}  Shows more detailed description of item.
        (If no item specified will show detailed description of area.)
    Go {LOCATION}   Goes to the specified location name if possible.
    Use {ITEM}      Uses specified item if in inventory or interactable object.
    Inventory       Displays contents of user inventory.
    Help            Shows this help screen.
Commands are accepted in upper or lower case and partial name matches count."""

# Function to clear display after input
def Clear():
    os.system('cls')

# Wrapper around randint cause I'm lazy
def GetRand(a,b):
    value = random.randint(a,b)
    return value

# Function to look through inventory
def BrowseInventory():
    print "You have the following items in your inventory:"
    for item in GPlay.Inventory:
        print item.Name

# Funtion to display valid room transitions
def GetTransitions(location):
    for t in GLoc.Transitions[location]:
        print CL.Fore.GREEN + CL.Style.BRIGHT + t.Name

# Function to calculate enemy hit/miss
def EnemyAttack(Entity):
    print CL.Fore.RED + "The " + Entity.Name + " is going to attack!\n"
    if GetRand(1, 100) < GetRand(Entity.HitRate[0], Entity.HitRate[1]):
        HitValue = GetRand(Entity.BaseDamage[0], Entity.BaseDamage[1])
        GPlay.Health -= HitValue
        print "It hits for " + HitValue + "!"
    else:
        print "It misses!"

# Define getting user input
def GetInput():
    strInput = raw_input(CL.Fore.YELLOW + "What would you like to do: ")
    Clear()
    if len(strInput) < 2:
        print "Sorry, I didn't understand that.\n"
        return
    listInput = strInput.rsplit()
    if (len(listInput) > 1) and (listInput[0].lower() in ["get", "take"]):
        return "GetItem", strInput.replace(listInput[0] + " ","")
    elif (len(listInput) > 1) and (listInput[0].lower() in ["look", "examine", "inspect"]):
        return "ExamineItem", strInput.replace(listInput[0] + " ","")
    elif (len(listInput) > 1) and (listInput[0].lower() in ["go", "exit", "goto", "to"]):
        return "GotoLocation", strInput.replace(listInput[0] + " ","")
    elif (len(listInput) > 1) and (listInput[0].lower() in ["use", "wield", "eat"]):
        return "UseItem", strInput.replace(listInput[0] + " ","")
    elif (len(listInput) == 1) and (listInput[0].lower() in ["inventory", "bag", "items"]):
        return "BrowseInventory", GPlay.Inventory
    elif (len(listInput) == 1) and (listInput[0].lower() in ["look", "examine", "inspect"]):
        return "ExamineLocation", location
    elif (len(listInput) == 1) and (listInput[0].lower() in ["help", "idk", "what"]):
        return "Help", None
    else:
        print "Hmm, try using words like take, examine, go, or use, it'll help me out!\nOr try typing help for some of that!\n"

# Game Start Sequence
print """Your eyes slowly open, through groggy and scattered thoughts you
begin to gather your senses. You're lying on a slightly lumpy couch, the
air in this room is the temperature and consistency of day old milk in a
cereal bowl, so not very nice...

As you look around you can see some bland surroundings in the haze. There
is a TV playing some kind of sci-fi show at low volume, there's a light
film of dust over most everything you can see. A coffee table, small bookshelf
other miscellanous living room flora and fauna, you know the drill...

Well, better stand up and get started! You can type 'help' to get some
insight as to what you can do, but mostly just try to do things outside
of the norm! Break this baby and tell me about it! You're my testers to
see if this framework actually works, thanks!
"""

# Main Game Loop
GameOn = True
location = GLoc.myLivingRoom
loopCounter = 0
while GameOn == True:
    loopCounter += 1
    if GPlay.Health <= 0:
        print CL.Fore.RED + "You have died =("
        print CL.Fore.RED + "It took you " + str(loopCounter) + " turns to die!"
        GameOn = False
        blah = raw_input(CL.Fore.RED + "Press enter to close!")
        break

    # ADD ATTACK SEQUENCE HERE #

    print CL.Fore.MAGENTA + CL.Style.BRIGHT + "You're in the " + location.Name
    print CL.Fore.MAGENTA + CL.Style.BRIGHT + location.ShortDesc
    print CL.Fore.GREEN + CL.Style.BRIGHT + "\nYou can go to these places:"
    GetTransitions(location)
    print ""

    print CL.Fore.RED + CL.Style.BRIGHT + "Your current health is: " + str(GPlay.Health) + "\n"

    tupleInput = GetInput()
    if not tupleInput:
        pass
    elif tupleInput[0] == "Help":
        print helpMessage + "\n"
    elif tupleInput[0] == "ExamineLocation":
        print "Let's take a look around the area..."
        print location.LongDesc + "\n"
    elif tupleInput[0] == "BrowseInventory":
        BrowseInventory()
        print ""
    elif tupleInput[0] == "GetItem":
        invChange = False
        for item in location.DynObjs:
            if (re.search(r"\b" + tupleInput[1], item.Name, re.I)):
                if item in GPlay.Inventory:
                    print "You already have that item!\n"
                    invChange = True
                else:
                    GPlay.Inventory.append(item)
                    location.DynObjs.remove(item)
                    usable = item()
                    usable.PickUp()
                    invChange = True
                    print "You picked up " + item.Name + "!\n"
                    break
        if invChange == False:
            print "Can't see any items like that in this area...\n"
    elif tupleInput[0] == "ExamineItem":
        examined = False
        for item in location.DynObjs:
            if (re.search(r"\b" + tupleInput[1], item.Name, re.I)) and examined == False:
                print item.ShortDesc + "\n"
                examined = True
        for item in location.StatObjs:
            if (re.search(r"\b" + tupleInput[1], item.Name, re.I)) and examined == False:
                print item.LongDesc + "\n"
                examined = True
        for item in GPlay.Inventory:
            if (re.search(r"\b" + tupleInput[1], item.Name, re.I)) and examined == False:
                print item.LongDesc + "\n"
                examined = True
        if examined == False:
            print "Hmm, nothing like that seems important in here...\n"
    elif tupleInput[0] == "GotoLocation":
        oldLoc = location
        for t in GLoc.Transitions[location]:
            if re.search(r"\b" + tupleInput[1], t.Name, re.I):
                location = t
                print "You go to the " + t.Name + "\n"
                break
        if oldLoc == location:
            print "Hmm, can't seem to go there right now.\n"
    elif tupleInput[0] == "UseItem":
        used = False
        for item in GPlay.Inventory:
            if (re.search(r"\b" + tupleInput[1], item.Name, re.I)) and used == False:
                if item.UsableObj in location.StatObjs:
                    usable = item()
                    usable.Use()
                    used = True
                elif item.UsableObj == "Any":
                    usable = item()
                    usable.Use()
                    used = True
        for item in location.DynObjs:
            if (re.search(r"\b" + tupleInput[1], item.Name, re.I)) and used == False:
                print "We haven't picked that up yet!\n"
                used = True
        for item in location.StatObjs:
            if (re.search(r"\b" + tupleInput[1], item.Name, re.I)) and used == False:
                if item.UsableObj in GPlay.Inventory or item.UsableObj == None:
                    usable = item()
                    usable.Use()
                    used = True
        if used == False:
            print "Hmm, nothing like that seems useful in here...\n"

    if location == GLoc.Outside_StartHouse:
        print CL.Fore.GREEN + CL.Style.BRIGHT + "You win! All you had to do is get outside! (But was it worth the weight?)"
        print CL.Fore.GREEN + CL.Style.BRIGHT + "It took you " + str(loopCounter) + " turns to win!"
        blah = raw_input(CL.Fore.GREEN + CL.Style.BRIGHT + "Press enter to close!")
        GameOn = False
