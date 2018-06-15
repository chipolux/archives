# -*- coding: utf-8 -*-
"""
Created on Thu May 16 01:57:04 2013

@author: chipolux
"""
import warnings
warnings.simplefilter('ignore')
import pyglet
from pyglet.gl import *
import mapping

MAP = 'room1'

window = pyglet.window.Window(800, 600, caption='Main Window', visible=False)

@window.event
def on_draw():
    global MAP
    level = mapping.Level(MAP)
    window.clear()
    level.batch.draw()

if __name__ == '__main__':
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    window.set_visible()
    pyglet.app.run()