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
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # set the background image to 0 in the image blank
    # and the size (10 x 8 tiles of size 16 x 16)
    background = stage.Grid(image_bank_background, 10, 8)
    
    # a sprite that will update every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)
    
    # set the background to image 0 in the image blanks
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display,60)
    # set the layer of all sprites, item show up in order
    game.layers = [ship] + [background]
    # render all sprites
    # most likely you will only render the background once per game
    game.render_block()
    
    # repeat forever, game loop
    while True:
        pass # just a placeholder for now
        # get user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X:
            print("A")
        if keys & ugame.K_O:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_RIGHT:
            ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT:
            ship.move(ship.x - 1, ship.y)
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)    
        
        # update game logic
        
        # redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
  
