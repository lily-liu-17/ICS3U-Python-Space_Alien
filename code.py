#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program is the "Space Aliens" program on the EdgeBadge

import ugame
import stage

import constants

def game_scene():
    # this function is he main game game_scene
    
    # image blanks for circut python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # set the background image to 0 in the image blank
    # and the size (10 x 8 tiles of size 16 x 16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    
    # a sprite that will update every frame
    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    
    # set the background to image 0 in the image blanks
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, constants.FPS)
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
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
                
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass    
        
        # update game logic
        
        # redraw sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()
