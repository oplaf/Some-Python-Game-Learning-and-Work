
import arcade
from Comp151Window import Comp151Window
import types


def update(game_window, delta_time):

    for bad_guy in game_window.bad_guys:
        bad_guy.center_x += game_window.bad_guyDx
    width, height = game_window.get_size()
    if game_window.bad_guys[-1]._get_right() > width:
        game_window.bad_guyDx = -game_window.bad_guyDx
    elif game_window.bad_guys[0]._get_left() < 0:
        game_window.bad_guyDx = -game_window.bad_guyDx


def draw(window):
    arcade.start_render()
    for bad_guy in window.bad_guys:
        bad_guy.draw()
    window.player.draw()


def setup(window):

    window.bad_guyDx = 3
    bad_guy_list = []
    for number in range(8):
        sprite_pos = number*72+40
        bad_guy = arcade.Sprite("direwolver-attack.png")
        bad_guy.set_position(sprite_pos, 700)
        bad_guy_list.append(bad_guy)
    player = arcade.Sprite("horseman-ne-attack1.png")
    player.set_position(500, 120)
    window.player = player
    window.bad_guys = bad_guy_list

def main():

    game_window = Comp151Window(1000,800, "Project 7 Demo")
    arcade.set_background_color(arcade.color.DEEP_MOSS_GREEN)
    setup(game_window)
    game_window.on_draw=types.MethodType(draw,game_window)
    game_window.on_update = types.MethodType(update, game_window)
    arcade.run()



if __name__ == '__main__':

    main()



