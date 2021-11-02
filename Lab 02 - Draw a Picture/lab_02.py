# setup
import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# defining functions

def draw_water():
    """coloring layers of water"""
    arcade.draw_lrtb_rectangle_filled(0, 600, 175, 135, (0, 62, 179)) # lighter blue (layer 7)
    arcade.draw_lrtb_rectangle_filled(0, 600, 225, 175, (0, 68, 204)) # even lighter blue (layer 8)
    arcade.draw_lrtb_rectangle_filled(0, 600, 275, 225, (0, 77, 230)) # lightest blue (layer 9)
    arcade.draw_lrtb_rectangle_filled(0, 600, 20, 10, (0, 9, 26)) # darkest blue (layer 1)
    arcade.draw_lrtb_rectangle_filled(0, 600, 35, 20, (0, 18, 51)) # darker blue (layer 2)
    arcade.draw_lrtb_rectangle_filled(0, 600, 45, 35, (0, 27, 77)) # dark blue (layer 3)
    arcade.draw_lrtb_rectangle_filled(0, 600, 70, 45, (0, 36, 102)) # medium dark blue (layer 4)
    arcade.draw_lrtb_rectangle_filled(0, 600, 100, 70, (0, 45, 128)) # darkish blue (layer 5)
    arcade.draw_lrtb_rectangle_filled(0, 600, 135, 100, (0, 54, 153)) # medium blue (layer 6)


def draw_stars():
    """creates stars"""
    arcade.draw_circle_filled(1, 550, 3, (255, 255, 153))
    arcade.draw_circle_filled(30, 500, 3, (255, 255, 230))
    arcade.draw_circle_filled(90, 300, 3, (255, 255, 153))
    arcade.draw_circle_filled(150, 400, 3, (255, 255, 230))
    arcade.draw_circle_filled(170, 550, 3, (255, 255, 230))
    arcade.draw_circle_filled(230, 476, 3, (255, 255, 153))
    arcade.draw_circle_filled(270, 360, 3, (255, 255, 230))
    arcade.draw_circle_filled(300, 380, 3, (255, 255, 230))
    arcade.draw_circle_filled(340, 570, 3, (255, 255, 230))
    arcade.draw_circle_filled(370, 589, 3, (255, 255, 153))
    arcade.draw_circle_filled(400, 580, 3, (255, 255, 230))
    arcade.draw_circle_filled(416, 475, 3, (255, 255, 230))
    arcade.draw_circle_filled(460, 598, 3, (255, 255, 153))
    arcade.draw_circle_filled(480, 471, 3, (255, 255, 230))
    arcade.draw_circle_filled(515, 327, 3, (255, 255, 230))
    arcade.draw_circle_filled(540, 330, 3, (255, 255, 153))
    arcade.draw_circle_filled(570, 450, 3, (255, 255, 153))
    arcade.draw_circle_filled(50, 429, 3, (255, 255, 230))
    arcade.draw_circle_filled(427, 438, 4, (255, 255, 230))
    arcade.draw_circle_filled(349, 548, 4, (255, 255, 230))
    arcade.draw_circle_filled(290, 308, 4, (255, 255, 230))
    arcade.draw_circle_filled(590, 418, 4, (255, 255, 230))
    arcade.draw_circle_filled(530, 590, 4, (255, 255, 230))
    arcade.draw_circle_filled(210, 418, 4, (255, 255, 230))
    arcade.draw_circle_filled(100, 330, 4, (255, 255, 230))


def draw_moon():
    """draws moon and craters"""
    # creating moon base
    arcade.draw_circle_filled(100, 500, 70, (255, 255, 128)) # shadow layer (1)
    arcade.draw_ellipse_filled(100, 500, 130, 140, (255, 255, 153), 30, 200) # shadow layer (2)
    arcade.draw_ellipse_filled(100, 500, 125, 140, (255, 255, 179), 30, 200) # shadow layer (3)
    arcade.draw_ellipse_filled(100, 500, 120, 140, (255, 255, 230), 30, 200) # shadow layer (4)
    arcade.draw_ellipse_filled(100, 500, 100, 135, (255, 255, 230), 30, 200) # light layer

    # creating moon craters
    arcade.draw_polygon_filled(((50, 530),
                                (70, 520),
                                (90, 537),
                                (60, 555),
                                (75, 557)
                                ),
                                (230, 243, 255))
    arcade.draw_polygon_filled(((60, 490),
                                (50, 500),
                                (67, 497),
                                (46, 515),
                                (55, 485)
                                ),
                                (230, 243, 255))
    arcade.draw_polygon_filled(((120, 500),
                                (137, 480),
                                (140, 497),
                                (129, 525),
                                (133, 467)
                                ),
                                (230, 243, 255))
    arcade.draw_polygon_filled(((115, 480),
                                (100, 440),
                                (110, 457),
                                (99, 495),
                                (116, 437)
                                ),
                                (217, 217, 217))
    arcade.draw_polygon_filled(((90, 460),
                                (77, 450),
                                (80, 467),
                                (79, 445),
                                (93, 457)
                                ),
                                (217, 217, 217))
    arcade.draw_polygon_filled(((70, 450),
                                (67, 480),
                                (56, 467),
                                (69, 505),
                                (53, 457)
                                ),
                                (217, 217, 217))
    arcade.draw_polygon_filled(((128, 500),
                                (150, 480),
                                (149, 497),
                                (139, 525),
                                (143, 467)
                                ),
                                (230, 243, 255))


def draw_boat(x):
    """draws boat"""
    arcade.draw_ellipse_filled(300 + x, 200, 500, 150, (102, 53,0)) # boat base
    arcade.draw_lrtb_rectangle_filled(0 + x, 600 + x, 140, 135, (0, 62, 179)) # lighter blue (layer 7)
    arcade.draw_lrtb_rectangle_filled(0 + x, 600 + x, 135, 120, (0, 54, 153)) # medium blue (layer 6)
    arcade.draw_ellipse_filled(300 + x, 205, 477, 45, (26, 13, 0)) # hollow of boat (1)
    arcade.draw_arc_filled(300 + x, 205, 477, 140, (51, 26, 0), 0, 180) # hollow of boat (2)
    arcade.draw_line(110 + x, 150, 490 + x, 150, (77, 40, 0)) # plank line
    arcade.draw_line(75 + x, 167, 525 + x, 167, (77, 40, 0)) # plank line
    arcade.draw_lrtb_rectangle_filled(225 + x, 255 + x, 260, 185, (102, 53, 0)) # boat seat
    arcade.draw_lrtb_rectangle_filled(345 + x, 375 + x, 260, 185, (102, 53, 0)) # boat seat


def draw_oar(x):
    """draws oar and reflections"""
    # drawing main oar
    arcade.draw_rectangle_filled(320 + x, 227, 200, 5, (26, 13, 0)) # oar length dark layer
    arcade.draw_rectangle_filled(320 + x, 229, 200, 5, (51, 26, 0)) # oar length lighter layer
    arcade.draw_rectangle_filled(320 + x, 230, 200, 3, (128, 66, 0)) # oar length light layer
    arcade.draw_rectangle_filled(223 + x, 227, 50, 30, (26, 13, 0)) # oar head dark layer
    arcade.draw_rectangle_filled(223 + x, 229, 50, 30, (51, 26, 0)) # oar head darker layer
    arcade.draw_rectangle_filled(223 + x, 231, 50, 28, (77, 40, 0)) # oar head lighter layer
    arcade.draw_rectangle_filled(223 + x, 232, 50, 26, (128, 66, 0)) # oar head lightest

    arcade.draw_polygon_filled(((202 + x, 238),
                                (212 + x, 242),
                                (220 + x, 243),
                                (217 + x, 236),
                                (208 + x, 241),
                                ),
                                (255, 255, 255))
    arcade.draw_polygon_filled(((202 + x, 238),
                                (200 + x, 232),
                                (203 + x, 233),
                                (210 + x, 236),
                                (205 + x, 235),
                                ),
                                (255, 255, 255))


def on_draw(delta_time):
    """draws everything"""
    arcade.start_render()

    draw_water()
    draw_moon()
    draw_stars()
    draw_boat(on_draw.boat_x)
    draw_oar(on_draw.boat_x)

    # setting animation increments
    on_draw.boat_x += 1

# setting initial coordinates
on_draw.boat_x = -600


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab_02")
    arcade.set_background_color(arcade.csscolor.BLACK)
    arcade.start_render()

    # calls on_draw every 60th of a second
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# call main function
main()