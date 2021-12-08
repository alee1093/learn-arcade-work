# setup
import arcade

# window variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def background():
    """drawing background"""
    x = 300
    while x <= SCREEN_WIDTH + 1000:
        arcade.draw_line(x + 250, 0, SCREEN_WIDTH - 500 - x, SCREEN_HEIGHT, (255, 204, 204), 1)
        x += 10


def gummy_guards():
    """drawing the gummy guards"""
    x = 20
    y = 400
    for i in range(3):
        arcade.draw_circle_filled(x - 10, y + 20, 7, (0, 128, 0))  # left ear
        arcade.draw_circle_filled(x + 10, y + 20, 7, (0, 128, 0))  # right ear
        arcade.draw_ellipse_filled(x, y, 25, 35, (0, 128, 0))  # torso
        arcade.draw_circle_filled(x, y + 12, 12, (0, 128, 0))  # head
        arcade.draw_circle_outline(x, y + 12, 12, (0, 102, 0))  # head outline
        arcade.draw_circle_filled(x - 5, y - 13, 7, (0, 102, 0))  # left foot
        arcade.draw_circle_filled(x + 9, y - 12, 6.5, (0, 102, 0))  # right foot
        arcade.draw_circle_filled(x - 6, y - 3, 7, (0, 102, 0))  # left arm
        arcade.draw_ellipse_filled(x + 13, y - 3, 20, 10, (0, 102, 0))  # right arm

        arcade.draw_line(x - 7, y + 17, x + 1, y + 14, (0, 0, 0), 3)  # left eyebrow
        arcade.draw_line(x + 4, y + 14, x + 7, y + 19, (0, 0, 0), 3)  # right eyebrow

        arcade.draw_circle_filled(x - 1, y + 10.5, 2.5, (0, 0, 0))  # left eye
        arcade.draw_circle_filled(x + 5.5, y + 11, 2.5, (0, 0, 0))  # right eye

        arcade.draw_line(x + 18, y - 20, x + 18, y + 15, (153, 51, 0), 3)  # spear shaft
        arcade.draw_triangle_filled(x + 12, y + 9, x + 24, y + 9, x + 18, y + 20, (191, 191, 191))  # spear head

        x += 50
        y -= 33


def gummy_worm():
    """draws gummy worm"""
    arcade.draw_ellipse_filled(500, 222, 90, 60, (0, 204, 255), 30)  # head
    arcade.draw_rectangle_filled(450, 230, 80, 40, (0, 204, 255), 350)  # first part of body
    arcade.draw_rectangle_filled(380, 235, 80, 30, (0, 204, 255), 30)  # second part of body
    arcade.draw_ellipse_filled(450, 230, 100, 50, (0, 204, 255), 350)  # first joint
    arcade.draw_ellipse_filled(380, 235, 100, 43, (0, 204, 255), 30)  # second joint
    arcade.draw_triangle_filled(340, 250, 355, 268, 220, 270, (0, 204, 255))
    arcade.draw_line(490, 230, 500, 240, (0, 0, 0), 3)  # left eyebrow
    arcade.draw_line(505, 242, 517, 240, (0, 0, 0), 3)  # right eyebrow

    arcade.draw_circle_filled(500, 225, 5, (0, 0, 0))  # left eye
    arcade.draw_circle_filled(517, 232, 5, (0, 0, 0))  # right eye


def peppermint_player():
    x1 = -10
    y1 = 40
    x2 = 0
    y2 = 40

    arcade.draw_line(490, 360, 440, 280, (0, 0, 0), 5)  # right arm

    arcade.draw_circle_outline(435, 294, 42, (230, 0, 0), 18)  # red part
    arcade.draw_circle_filled(450, 290, 40, (250, 250, 250))  # base
    arcade.draw_circle_outline(450, 290, 40, (230, 0, 0), 10)  # red part

    arcade.draw_line(420, 245, 405, 290, (0, 0, 0), 5)  # left arm
    arcade.draw_ellipse_filled(491, 365, 15, 25, (250, 250, 250), 17)  # right hand
    arcade.draw_ellipse_filled(425, 235, 15, 25, (250, 250, 250), 320)  # left hand


def trees():
    """draws trees"""
    x = 20
    y = 630

    for i in range (5):
        arcade.draw_triangle_filled(x, y - 20, x - 100, y - 200, x + 100, y - 200, (255, 153, 153))  # second layer
        arcade.draw_triangle_filled(x, y, x - 60, y - 100, x + 60, y - 100, (255, 179, 179))  # first layer
        x += 150
        y -= 30

    x = 10
    y = 350
    for i in range (5):
        arcade.draw_triangle_filled(x, y - 20, x - 100, y - 200, x + 100, y - 200, (255, 153, 153))  # second layer
        arcade.draw_triangle_filled(x, y, x - 60, y - 100, x + 60, y - 100, (255, 179, 179))  # first layer
        x += 150
        y -= 80


def main():
    """main code"""
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Gummy Thief")
    arcade.set_background_color((255, 128, 128))

    arcade.start_render()
    background()
    trees()
    gummy_guards()
    gummy_worm()
    peppermint_player()
    arcade.finish_render()
    arcade.run()


# execution
main()
