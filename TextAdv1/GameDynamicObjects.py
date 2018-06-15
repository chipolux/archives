# -*- coding: utf-8 -*-
"""
GameDynamicObjects Module
Contains information on all dynamic game objects.

Created on Mon Sep 10 19:39:11 2012

@author: chipolux
"""
import GameLocations as GLoc
import GameStaticObjects as GSObj
import GamePlayer as GPlay

class Book_1:
    Name = "Worn Book"
    ShortDesc = "A worn looking book, the title seems to say something about cats..."
    LongDesc = "'How To Potty Train Your Pussy!' Is this a book about potty training cats or?!"
    UsableObj = GSObj.BookShelf_1
    def Use(self):
        GPlay.Inventory.remove(Book_1)
        GLoc.Transitions[GLoc.myKitchen].append(GLoc.mySecretRoom)
        GLoc.myKitchen.ShortDesc = "Looks like something with the bookshelf moved the fridge!"
        GLoc.myKitchen.LongDesc = "The fridge has moved along tracks hidden in the wall, there is a small\nroom hidden behind it!"
        print "Let's put this book on the shelf!"
        print "There was a strange noise in the kitchen...\n"
    def PickUp(self):
        GLoc.myLivingRoom.LongDesc = "There is a coffee table and a small bookshelf in the corner as well as a sofa."

class Book_2:
    Name = "Dusty Book"
    ShortDesc = "Dusy book, doesn't look like it's been moved in some time."
    LongDesc = "'How To Shave A Beaver' Okay, I'm just going to assume these books are a zookeeers or something..."
    UsableObj = None
    def Use(self):
        pass
    def PickUp(self):
        pass

class Key_1:
    Name = "Front Door Key"
    ShortDesc = "Looks like a key to a door in this house."
    LongDesc = "It's a key to the front door! Now we can escape this dingy house!"
    UsableObj = None
    def Use(self):
        pass
    def PickUp(self):
        GLoc.Transitions[GLoc.myFrontDoor].append(GLoc.Outside_StartHouse)
        GLoc.myFrontDoor.ShortDesc = "We've got the key so out we go! No telling where our feet'll take us..."
        GLoc.myFrontDoor.LongDesc = "Since we found the key we can get in and out anytime we want!"

class Sandwich_1:
    Name = "Turkey Sandwich"
    ShortDesc = "Plain turkey sandwich, delicious!"
    LongDesc = "A delicious sandwich, turkey, lettuce, tomato, anchovies, everything and more!"
    UsableObj = "Any"
    def Use(self):
        print "You eat the delicious sandwich like some kind of sick walrus!"
        print "Your health is increased by 15!\n"
        GPlay.Health += 15
        GPlay.Inventory.remove(Sandwich_1)
    def PickUp(self):
        GLoc.myKitchen.LongDesc = "Not much in here, just a soggy spot on the floor, looks like a walrus picked\nup a sandwich there."

class Poison_1:
    Name = "Bottle of Poison"
    ShortDesc = "Just a little bottle of poison."
    LongDesc = "Says, 'KILL-EM-DEAD, Poison to kill just about anything.' Sounds like strong stuff."
    UsableObj = "Any"
    def Use(self):
        print "You down the whole bottle like a depressed father who's just lost his\nfamily in a messy divorce."
        print "Your health is decreased by 1000!\n"
        GPlay.Health -= 1000
        GPlay.Inventory.remove(Poison_1)
    def PickUp(self):
        GLoc.myBedroom.LongDesc = "There's a messy bed, old newspaper clippings taped to the wall,\nnothing interesting here."