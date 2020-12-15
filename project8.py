import arcade
import Comp151Window
import types
import random
import time


def update(window, delta_time):
    for bad_guy in window.bad_guys:
        bad_guy.center_x += window.bad_guyDx

    width, height = window.get_size()

    if window.bad_guys[-1]._get_right() > width:
        window.bad_guyDx = -window.bad_guyDx
    elif window.bad_guys[0]._get_left() < 0:
        window.bad_guyDx = -window.bad_guyDx


    for bad_guy in window.bad_guys:
        if bad_guy.collides_with_sprite(window.player):
            print(f"Don't touch the bad guys!")

    for bullet in window.lots_bullets:
        if bullet.collides_with_sprite(window.player):
            bullet.remove_from_sprite_lists()
            window.score -= 5
            window.player_ouch.play()
            create_new_badguy_bullet(window)
            window.health_amount -= 1


        if bullet.top < 0:
            bullet.remove_from_sprite_lists()
            create_new_badguy_bullet(window)

        window.lots_bullets.update()

    health_to_remove = None
    for health in window.healthBars:
        if bullet.collides_with_sprite(window.player):
            health_to_remove = health
            break
    if health_to_remove:
        window.healthBars.remove(health_to_remove)

    for laser in window.lots_lasers:
        for bad_guy in window.bad_guys:
            if laser.collides_with_sprite(bad_guy):
                bad_guy.remove_from_sprite_lists()
                laser.remove_from_sprite_lists()
                window.score += 10
                print(f"BAD GUY DEAD")


    window.lots_lasers.update()


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
    if window.space_pressed:
        window.lots_lasers
        create_new_good_bullet(window)

        window.space_pressed = False
    if window.escape_pressed:
        exit()
    window.player.center_x = window.player.center_x + window.playerDx
    window.player.center_y = window.player.center_y + window.playerDy


    coin_to_remove = None
    for coin_pile in window.coinList:
        if coin_pile.collides_with_sprite(window.player):
            window.score += 10
            window.coin_sound.play()
            print(f"your score is {window.score}")
            coin_to_remove = coin_pile
            break

    if coin_to_remove:
        window.coinList.remove(coin_to_remove)

def create_new_badguy_bullet(window):
    BULLET_SPEED = -20

    rand = random.randint(0, len(window.bad_guys) -1)
    bad_guy = window.bad_guys[rand]

    bullet = arcade.Sprite("laserBlue01.png")
    bullet.center_x = bad_guy.center_x
    bullet.angle = 180
    bullet.top = bad_guy.bottom
    bullet.change_y = BULLET_SPEED

    window.lots_bullets.append(bullet)



def create_new_good_bullet(window):
    player = window.player

    your_laser = arcade.Sprite("laserBlue01.png")
    your_laser.center_x = player.center_x
    your_laser.angle = 0
    your_laser.bottom = player.top
    your_laser.change_y = 5
    window.lots_lasers.append(your_laser)

    #for your_laser in




def draw(window_being_updated):
    # update(window_being_updated)
    arcade.start_render()

   # for health_amount in
    for bad_guy in window_being_updated.bad_guys:
        bad_guy.draw()
    for coin_pile in window_being_updated.coinList:
        coin_pile.draw()
    for health in window_being_updated.healthBars:
        health.draw()
    for bullet in window_being_updated.lots_bullets:
        bullet.draw()
    for your_laser in window_being_updated.lots_lasers:
        your_laser.draw()
    if window_being_updated.health_amount <= 0:
        arcade.draw_text("GAME OVER", 300, 400, arcade.color.RED, 50)
        arcade.draw_text("Thanks for playing! Press ESC to exit game. ", 150, 200, arcade.color.WHITE, 25)


    arcade.draw_text(f"Score: {window_being_updated.score}", 900, 20, arcade.color.WHITE, 14)

    arcade.draw_text(f"Health: {window_being_updated.health_amount}", 10, 60, arcade.color.WHITE, 14)

    window_being_updated.player.draw()




def setup_window(graphicsWindow):

    bad_guy_list = arcade.SpriteList()
    player_list = arcade.SpriteList()
    coin_list = arcade.SpriteList()
    bullet_list = arcade.SpriteList()
    health_list = arcade.SpriteList()
    your_laser_list = arcade.SpriteList()

    graphicsWindow.bad_guyDx = 3
    #bad_guy_list = []
    bad_guy_amount = 8
    for number in range(bad_guy_amount):
        sprite_pos = number*100+40
        bad_guy = arcade.Sprite("direwolver-attack.png")
        bad_guy.set_position(sprite_pos, 700)
        bad_guy_list.append(bad_guy)


    #coin_list = []
    width, height = graphicsWindow.get_size()
    coin_number = 4
    for coin_count in range(coin_number):
        red_coin = arcade.Sprite("coinGold.png")
        xPos = random.randint(0, width)
        yPos = random.randint(0, height)
        red_coin.set_position(xPos, yPos)
        coin_list.append(red_coin)


    #health_list = []
    health_number = 1
    for number in range(health_number):
        health_pos = number*80+40
        health = arcade.Sprite("gemRed.png")
        health.set_position(health_pos, 30)
        health_list.append(health)
    graphicsWindow.health_amount = health_number


    graphicsWindow.bulletDx = -2

    bullet = arcade.Sprite("laserBlue01.png")
    bullet.center_x = bad_guy.center_x
    bullet.angle = -180
    bullet.top = bad_guy.bottom
    bullet.change_y = -30
    bullet_list.append(bullet)
    bullet_sound = arcade.Sound("laser1sound.wav")
    graphicsWindow.bullet_sound = bullet_sound


    player = arcade.Sprite("galleon.png")
    player.set_position(200, 400)
    graphicsWindow.player = player
    player_list.append(player)


 #   your_laser = arcade.Sprite("laserBlue01.png")
 #   your_laser.center_x = player.center_x
 #   your_laser.angle = 0
 #   your_laser.bottom = player.top
 #   your_laser.change_y = 5
 #   your_laser_list.append(your_laser)
 #   your_laser_sound = arcade.Sound("laser1sound.wav")
 #   graphicsWindow.your_laser_sound = your_laser_sound


    arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)

    graphicsWindow.playerDx = 0
    graphicsWindow.playerDy = 0

    graphicsWindow.coinList = coin_list
    graphicsWindow.bad_guys = bad_guy_list
    graphicsWindow.healthBars = health_list
    graphicsWindow.lots_bullets = bullet_list
    graphicsWindow.lots_lasers = your_laser_list
    graphicsWindow.the_player = player_list

    graphicsWindow.score = 0

    graphicsWindow.up_pressed = False
    graphicsWindow.down_pressed = False
    graphicsWindow.left_pressed = False
    graphicsWindow.right_pressed = False
    graphicsWindow.space_pressed = False
    graphicsWindow.escape_pressed = False


    coin_sound = arcade.Sound("coin5.wav")
    graphicsWindow.coin_sound = coin_sound
    player_loser = arcade.Sound("gameover5.wav")
    graphicsWindow.player_loser = player_loser
    player_winner = arcade.Sound("gameoverwinner.wav")
    graphicsWindow.player_winner = player_winner
    player_ouch = arcade.Sound("player_getting_hit.wav")
    graphicsWindow.player_ouch = player_ouch





def key_pressed(game_window, key, modifiers):

    if key == arcade.key.LEFT:
        game_window.left_pressed = True
    if key == arcade.key.RIGHT:
        game_window.right_pressed = True
    if key == arcade.key.UP:
        game_window.up_pressed = True
    if key == arcade.key.DOWN:
        game_window.down_pressed = True
    if key == arcade.key.SPACE:
        game_window.space_pressed = True
    if key == arcade.key.ESCAPE:
        game_window.escape_pressed = True


def key_released(game_window, key, modifiers):

    if key == arcade.key.LEFT:
        game_window.left_pressed = False
    if key == arcade.key.RIGHT:
        game_window.right_pressed = False
    if key == arcade.key.UP:
        game_window.up_pressed = False
    if key == arcade.key.DOWN:
        game_window.down_pressed = False
    if key == arcade.key.SPACE:
        game_window.space_pressed = False
    if key == arcade.key.ESCAPE:
        game_window.escape_pressed = False


def main():

    graphicsWindow = Comp151Window.Comp151Window(1000, 800, "Final Project")
    setup_window(graphicsWindow)
    graphicsWindow.on_draw = types.MethodType(draw, graphicsWindow)
    graphicsWindow.on_update = types.MethodType(update, graphicsWindow)
    graphicsWindow.on_key_press = types.MethodType(key_pressed, graphicsWindow)
    graphicsWindow.on_key_release = types.MethodType(key_released, graphicsWindow)
    arcade.run()

main()