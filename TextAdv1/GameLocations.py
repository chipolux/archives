# -*- coding: utf-8 -*-
"""
GameLocations Module
Contains information on locations and their transitions.

Created on Sat Sep 15 11:05:27 2012

@author: chipolux
"""
import GameDynamicObjects as GDObj
import GameStaticObjects as GSObj

class myLivingRoom:
    Name =      "Living Room"
    ShortDesc = "Where it began, an episode of Doctor Who is playing on the TV.\nBest not to blink..."
    LongDesc =  "There is a coffee table with a book on it, a small bookshelf in\nthe corner as well as a sofa."
    DynObjs =   [GDObj.Book_1]
    StatObjs =  [GSObj.BookShelf_1]

class myHallway:
    Name =      "Hallway"
    ShortDesc = "This could take you anywhere! Well, anywhere in the house or to\nthe front door of course..."
    LongDesc =  "Ahh, the good old hallway, a few pictures of fat old men on the wall,\nan umbrella stand, doors to other rooms. It's got it all!"
    DynObjs =   []
    StatObjs =  []

class myKitchen:
    Name =      "Kitchen"
    ShortDesc = "Mmm, maybe we should make a sandwich! But I have been gaining weight\nrecently..."
    LongDesc = "Looks like there's a sandwich in the corner... You're not that hungry are you?\nThe fridge has some strange scrapes on the floor near it, can't get it to budge though."
    DynObjs =   [GDObj.Sandwich_1]
    StatObjs =  []

class myBedroom:
    Name =      "Bedroom"
    ShortDesc = "*Yawn* Perhaps I should take a quick nap? Nah, feels like adventure\nis afoot!"
    LongDesc =  "There's a messy bed, a bottle of pills, old newspaper clippings taped to\nthe wall, nothing interesting here."
    DynObjs =   [GDObj.Poison_1]
    StatObjs =  [GSObj.Bedroom_Clippings]

class myFrontDoor:
    Name =      "Front Door"
    ShortDesc = "You know what they say, be careful stepping out your front door, you\ncould trip. But it's locked for now!"
    LongDesc =  "There's a simple lock on the front door, kinda dusty. Looks like no one\nhas been in or out in awhile."
    DynObjs =   []
    StatObjs =  []

class mySecretRoom:
    Name =      "Secret Room"
    ShortDesc = "A tiny room behind the fridge, how odd! It's really dusty and dark, better\ntake a close look around."
    LongDesc =  "There is a film of dust everywhere, it looks like there's a key on the floor..."
    DynObjs =   [GDObj.Key_1]
    StatObjs =  []

class Outside_StartHouse:
    Name =      "Outside"
    ShortDesc = "Just outside the front door of the starting house! Looks like we can\ngo anywhere... well almost."
    LongDesc =  "NO DESCRIPTION! Send me one, I feed on yo ideas boi!"
    DynObjs =   []
    StatObjs =  []

# Location Transition Dictionary
Transitions = {
    myHallway: [myKitchen, myBedroom, myLivingRoom, myFrontDoor],
    myLivingRoom: [myHallway],
    myKitchen: [myHallway],
    myBedroom: [myHallway],
    myFrontDoor: [myHallway],
    mySecretRoom: [myKitchen]
}