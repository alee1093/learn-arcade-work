import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_miscellaneous(x, y):
    """draws units behind"""
    arcade.draw_line(300 + x, 215 + y, 330 + x, 260 + y, arcade.csscolor.BLACK, 5) # right upper arm
    arcade.draw_ellipse_outline(315 + x, 350 + y, 20, 35, arcade.csscolor.BLACK, 1, 335) # left hand fill


def draw_head(x, y):
    """draws head"""
    arcade.draw_circle_filled(300 + x, 300 + y, 50, (255, 219, 172)) # base fill
    arcade.draw_circle_outline(300 + x, 300 + y, 50, (241, 194, 125)) # base outline
    arcade.draw_ellipse_filled(285 + x, 315 + y, 18, 30, (arcade.csscolor.BLACK)) # left eye
    arcade.draw_ellipse_filled(288 + x, 320 + y, 5, 10, (arcade.csscolor.WHITE)) # left eye glimmer1
    arcade.draw_ellipse_filled(320 + x, 315 + y, 18, 30, (arcade.csscolor.BLACK)) # right eye
    arcade.draw_ellipse_filled(323 + x, 320 + y, 5, 10, (arcade.csscolor.WHITE)) # right eye glimmer1
    arcade.draw_rectangle_outline(328 + x, 294 + y, 40, 20, (241, 194, 125 )) # nose: rectangle
    arcade.draw_rectangle_filled(313 + x, 294 + y, 30, 19, (255, 219, 172)) # nose: erase rectangle
    arcade.draw_ellipse_outline(343 + x, 294.5 + y, 45, 19.5, (241, 194, 125)) # nose: ellipse
    arcade.draw_ellipse_filled(342 + x, 294 + y, 45, 19.5, (255, 219, 172)) # nose: erase ellipse
    arcade.draw_ellipse_filled(303 + x, 270 + y, 16, 19, (204, 0, 0)) # mouth fill
    arcade.draw_ellipse_outline(303.3 + x, 270 + y, 16, 19, arcade.csscolor.BLACK, 2) # mouth outline


def draw_mustache(x, y):
    """draws mustache"""
    arcade.draw_ellipse_filled(303.5 + x, 276 + y, 30, 13, arcade.csscolor.GREY, 355)


def draw_hat(x, y):
    """draws hat"""
    arcade.draw_rectangle_filled(255 + x, 375 + y, 75, 90, arcade.csscolor.BLACK, 330) # rectangle base
    arcade.draw_arc_filled(232 + x, 414 + y, 70, 10, arcade.csscolor.BLACK, 0, 180, 30) # ellipse overlap
    arcade.draw_ellipse_filled(275.5 + x, 334.5 + y, 110, 8, arcade.csscolor.BLACK, 330) # ellipse overlap
    arcade.draw_line(245 + x, 320 + y, 307 + x, 355.5 + y, arcade.csscolor.WHITE, 0.3) # hat rim lining


def draw_body(x, y):
    """draws main body except for right arm"""
    arcade.draw_line(300 + x, 250 + y, 300 + x, 200 + y, arcade.csscolor.BLACK, 7) # torso
    arcade.draw_line(300 + x, 215 + y, 250 + x, 240 + y, arcade.csscolor.BLACK, 5) # left upper arm
    arcade.draw_line(250 + x, 240 + y, 240 + x, 293 + y, arcade.csscolor.BLACK, 3) # left lower arm
    arcade.draw_ellipse_filled(245 + x, 310 + y, 20, 40, arcade.csscolor.WHITE, 20) # right hand fill
    arcade.draw_ellipse_outline(245 + x, 310 + y, 20, 40, arcade.csscolor.BLACK, 1, 20) # right hand outline
    arcade.draw_line(300 + x, 200 + y, 286.5 + x, 165 + y, arcade.csscolor.BLACK, 7) # left leg
    arcade.draw_line(300 + x, 200 + y, 315 + x, 168 + y, arcade.csscolor.BLACK, 7) # right leg


def draw_shoes(x, y):
    """draws shoes"""
    arcade.draw_rectangle_filled(292.5 + x, 160 + y, 20, 15, arcade.csscolor.BLUE) # left foot rectangle fill
    arcade.draw_arc_filled(299.8 + x, 153 + y, 22, 28.5, arcade.csscolor.BLUE, 0, 180) # left foot arc filled
    arcade.draw_rectangle_filled(319.5 + x, 165 + y, 20, 15, arcade.csscolor.BLUE) # right foot rectangle fill
    arcade.draw_arc_filled(326.8 + x, 158 + y, 22, 28.5, arcade.csscolor.BLUE, 0, 180) # right foot arc filled


def on_draw(delta_time):
    """draw everything"""
    arcade.start_render()

    draw_miscellaneous(on_draw.miscellaneous, 0)
    draw_head(on_draw.head, 0)
    draw_mustache(on_draw.mustache, 0)
    draw_hat(on_draw.hat, 0)
    draw_body(on_draw.body, 0)
    draw_shoes(on_draw.shoes, 0)

    on_draw.miscellaneous += 1
    on_draw.head += 1
    on_draw.mustache += 1
    on_draw.hat += 1
    on_draw.body += 1
    on_draw.shoes += 1


on_draw.miscellaneous = 10
on_draw.head= 10
on_draw.mustache = 10
on_draw.hat = 10
on_draw.body = 10
on_draw.shoes = 10


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite 1")
    arcade.set_background_color((255, 255, 255))

    # calls on_draw every 60th of a second
    arcade.schedule(on_draw, 1/60)
    arcade.run()

main()