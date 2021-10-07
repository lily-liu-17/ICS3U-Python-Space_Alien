#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program is the "Space Aliens" program on the EdgeBadge

import ugame
import stage

def game_scene():
    # this function is he main game game_scene
    
    # image blanks for circut python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    
    # set the background image to 0 in the image blank
    # and the size (10 x 8 tiles of size 16 x 16)
    background = stage.Grid(image_bank_background, 10, 8)
    
    # set the background to image 0 in the image blanks
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display,60)
    # set the layer of all sprites, item show up in order
    game.layers = [background]
    # render all sprites
    # most likely you will only render the background once per game
    game.render_block()
    
    # repeat forever, game loop
    while True:
        pass # just a placeholder for now

if __name__ == "__main__":
    game_scene()
    
