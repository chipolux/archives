# -*- coding: utf-8 -*-
"""
Created on Sat Jun 08 17:52:59 2013

@author: chipolux
"""
import warnings
warnings.simplefilter('ignore')
import pyglet
from pyglet.window import key
from pyglet.gl import *
import mapping
import utils

# Load config file
config = utils.parse_jsonfile(utils.path.join(utils.CURRENT_DIR, 'map_viewer.config'))

# Set MAP to 1 for startup
MAP = config['Button_1']
LEVEL = mapping.Level(MAP)

# Create window
window = pyglet.window.Window(800, 600, caption='Map Viewer', visible=False)

# Update MAP on key press
@window.event
def on_key_press(symbol, modifiers):
    global MAP
    global LEVEL
    if symbol in range(key._0, key._9 + 1):
        n = symbol - key._0
        if config['Button_%s' % n] != '':
            MAP = config['Button_%s' % n]
            LEVEL = mapping.Level(MAP)

@window.event
def on_text_motion(motion):
    global LEVEL
    if motion == key.MOTION_UP:
        LEVEL.move(0, 5)
    elif motion == key.MOTION_DOWN:
        LEVEL.move(0, -5)
    elif motion == key.MOTION_LEFT:
        LEVEL.move(-5, 0)
    elif motion == key.MOTION_RIGHT:
        LEVEL.move(5, 0)

@window.event
def on_draw():
    global LEVEL
    window.clear()
    LEVEL.batch.draw()

if __name__ == '__main__':
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    window.set_visible()
    pyglet.app.run()