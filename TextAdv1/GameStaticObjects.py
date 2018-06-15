# -*- coding: utf-8 -*-
"""
GameStaticObjects Module
Contains information on all static objects.

Created on Sat Sep 15 14:58:21 2012

@author: chipolux
"""
import GameDynamicObjects as GDObj

class BookShelf_1:
    Name = "Small Bookshelf"
    ShortDesc = "Small bookshelf in the corner of the living room."
    LongDesc = "A few books about different various subjects, there's a spot missing a book\nthat looks extra worn..."
    UsableObj = None
    def Use(self):
        print "Can't use that right now.\n"

class Bedroom_Clippings:
    Name = "Newspaper Clippings"
    ShortDesc = "Some old newspaper clippings tacked to the wall."
    LongDesc = "This one is written over, says 'If she touches your dick, come immediately\nand then start farting.' How strange..."
    UsableObj = None
    def Use(self):
        print "Can't use that right now.\n"