# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:29:03 2013

@author: chipolux
"""
import pyglet
import utils

TILE_SETS = []

def load_tileset(path, width, height, x_offset, y_offset):
    '''Load tileset if not already in memory.'''
    if not path in [x['name'] for x in TILE_SETS]:
        name = path
        path = utils.path.join(utils.CURRENT_DIR, 'images', path)
        image = pyglet.image.load(path)
        column_count = image.width / width
        row_count = image.height / height
        tiles = pyglet.image.ImageGrid(image, row_count, column_count)
        TILE_SETS.append({'name': name,
                          'path': path,
                          'width': width,
                          'height': height,
                          'x_offset': x_offset,
                          'y_offset': y_offset,
                          'tiles': tiles.get_texture_sequence(),
                          'rows': row_count,
                          'columns': column_count})
        return len(TILE_SETS) - 1
    else:
        for n in range(len(TILE_SETS)):
            if TILE_SETS[n]['name'] == path:
                return n

class Level:
    '''Handle loading a set of level files and required tilesets.'''
    def __init__(self, level_name='room1'):
        '''Build paths to files, kick off parsing functions.'''
        map_path = utils.path.join(utils.CURRENT_DIR, 'maps', '%s.map' % level_name)
        obj_path = utils.path.join(utils.CURRENT_DIR, 'maps', '%s.obj' % level_name)
        
        # Initialize blocked
        self.blocked = []
        
        # Initialize groups and batch
        self.groups = []
        self.sprites = []
        self.batch = pyglet.graphics.Batch()
        
        # Parse files
        self._parse_mapfile(map_path)
        self._parse_objfile(obj_path)
        
        # Prep for drawing
        self._prep_batch()

    def _parse_mapfile(self, path):
        '''Extract map data from file and add to instance.'''
        if utils.path.exists(path):
            # Load json from file
            raw_json = utils.parse_jsonfile(path)

            # Parse out tile sources
            tilesets = []
            for n in range(raw_json['source_count']):
                path = raw_json['source%s_path' % n]
                x = raw_json['source%s_tilesize' % n][0]
                y = raw_json['source%s_tilesize' % n][1]
                x_offset = raw_json['source%s_offset' % n][0]
                y_offset = raw_json['source%s_offset' % n][1]
                index = load_tileset(path, x, y, x_offset, y_offset)
                tilesets.append(index)

            # Parse out map size
            self.map_size = raw_json['mapsize']

            # Parse out map tiles
            self.layer_count = raw_json['layer_count']
            self.tiles = []
            for n in range(self.layer_count):
                tiles = self._parse_tiles(raw_json['layer%s' % n], tilesets)
                self.tiles.append(tiles)
        else:
            raise IOError, 'Mapfile does not exist: %s' % path

    def _parse_objfile(self, path):
        '''Extract object data from file and add to instance.'''
        if utils.path.exists(path):
            # Load json from file
            raw_json = utils.parse_jsonfile(path)

            # Placeholder access for now
            self.obj_file = raw_json
        else:
            raise IOError, 'Objfile does not exist: %s' % path
            
    def _parse_tiles(self, tiles, tilesets):
        new_tiles = []
        for tile in tiles:
            new = {}
            new['coords'] = tile[0][0:2]
            new['tileset'] = tilesets[tile[1]]
            new['tile'] = tile[2]
            new['blocked'] = tile[3]
            if len(tile[0]) == 4:
                new['offset'] = tile[0][2:4]
            else:
                new['offset'] = [0, 0]
            new_tiles.append(new)
        new_tiles.reverse()
        return new_tiles
        
    def _prep_batch(self):
        for n in range(self.layer_count):
            self.groups.append(pyglet.graphics.OrderedGroup(n))
            for i in range(len(self.tiles[n])):
                index = self.tiles[n][i]['tileset']
                tile = self.tiles[n][i]['tile']
                x_size = TILE_SETS[index]['width']
                y_size = TILE_SETS[index]['height']
                x_coord = self.tiles[n][i]['coords'][0]
                y_coord = self.tiles[n][i]['coords'][1]
                x_offset = self.tiles[n][i]['offset'][0]
                y_offset = self.tiles[n][i]['offset'][1]
                x_offset = x_offset + (TILE_SETS[index]['x_offset'] * x_coord)
                y_offset = y_offset + (TILE_SETS[index]['y_offset'] * y_coord)
                x, y = (x_coord * x_size) + x_offset, (y_coord * y_size) + y_offset
                if self.tiles[n][i]['blocked']:
                    self.blocked.append([x, y])
                self.sprites.append(pyglet.sprite.Sprite(TILE_SETS[index]['tiles'][tile],
                                                         x, y,
                                                         batch = self.batch,
                                                         group = self.groups[-1]))
                                                         
    def move(self, x, y):
        for n in range(len(self.sprites)):
            old_x = self.sprites[n].x
            old_y = self.sprites[n].y
            new_x = old_x + x
            new_y = old_y + y
            self.sprites[n].set_position(new_x, new_y)
                                                         
    def is_blocked(self, x, y):
        if [x, y] in self.blocked:
            return True
        return False

class Tileset:
    def __init__(self, set_name, width, height):
        pass

if __name__ == '__main__':
    test_level = Level('room3')
    test_level.draw()
