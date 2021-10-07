#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program is the "Space Aliens" program on the EdgeBadge

import ugame
import stage

def game_scene():
    #this function is he main game game_scene

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display,60)
    game.layers = [background]
    game.render_block()
    
    # repeat forever, game loop
    while True:
        pass # just a placeholder for now

if __name__ == "__main__":
    game_scene()
   
