import arcade
import Comp151Window
import types
import random

def update(window, delta_time):










    if window.up_pressed and not window.down_pressed:
       window.playerDy = 3
    elif window.down_pressed and not window.up_pressed:
       window.playerDy = -3
    else:
        window.playerDy = 0
    if window.left_pressed and not window.right_pressed:
        window.playerDx = -3
    elif window.right_pressed and not window.left_pressed:
        window.playerDx = 3
    else:
        window.playerDx = 0

    window.player.center_x = window.player.center_x + window.playerDx
    window.player.center_y = window.player.center_y + window.playerDy
    dot_to_remove = None
    for dot_pile in window.dotList:
        if dot_pile.collides_with_sprite(window.player):
            window.score += 10
            window.ching_sound.play()
            print(f"your score is {window.score}")
            dot_to_remove = dot_pile
            break
    if dot_to_remove:
        window.dotList.remove(dot_to_remove)

def draw(window_being_updated):

    #update(window_being_updated)
    arcade.start_render()
    window_being_updated.player.draw()
    for dot_pile in window_being_updated.dotList:
        dot_pile.draw()



def setup_window(graphicsWindow):
    dot_list = []
    width, height = graphicsWindow.get_size()
    for dot_count in range(6):
        red_dot = arcade.Sprite("reddot.png")
        xPos = random.randint(0, width)
        yPos = random.randint(0, height)
        red_dot.set_position(xPos, yPos)
        dot_list.append(red_dot)

    player = arcade.Sprite("galleon.png")
    player.set_position(200, 400)
    graphicsWindow.player = player
    arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)
    graphicsWindow.playerDx = 0
    graphicsWindow.playerDy = 0
    graphicsWindow.dotList = dot_list
    graphicsWindow.up_pressed = False
    graphicsWindow.down_pressed = False
    graphicsWindow.left_pressed = False
    graphicsWindow.right_pressed = False
    graphicsWindow.score = 0
    ching_sound = arcade.Sound("Cash_register.ogg")
    graphicsWindow.ching_sound = ching_sound
    health = arcade.Sprite("health_bar.png")
    health.set_position(25,600)




def key_pressed(game_window, key, modifiers):
    if key == arcade.key.LEFT:
        game_window.left_pressed = True
    if key == arcade.key.RIGHT:
        game_window.right_pressed = True
    if key == arcade.key.UP:
        game_window.up_pressed = True
    if key == arcade.key.DOWN:
        game_window.down_pressed = True


def key_released(game_window, key, modifiers):
    if key == arcade.key.LEFT:
        game_window.left_pressed = False
    if key == arcade.key.RIGHT:
        game_window.right_pressed = False
    if key == arcade.key.UP:
        game_window.up_pressed = False
    if key == arcade.key.DOWN:
        game_window.down_pressed = False


def main():
    graphicsWindow = Comp151Window.Comp151Window(1000,800,"Final Project")
    setup_window(graphicsWindow)
    graphicsWindow.on_draw = types.MethodType(draw, graphicsWindow)
    graphicsWindow.on_update = types.MethodType(update, graphicsWindow)
    graphicsWindow.on_key_press = types.MethodType(key_pressed, graphicsWindow)
    graphicsWindow.on_key_release = types.MethodType(key_released, graphicsWindow)
    arcade.run()




main()