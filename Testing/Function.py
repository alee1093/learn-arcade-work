import arcade

# defining functions

def draw_circle(x, y, r):
    """draws a circle"""
    arcade.draw_circle_outline(x, y, r, arcade.csscolor.BLACK)


def draw_rectangle(x, y, w, h):
    """draws a rectangle"""
    arcade.draw_rectangle_outline(x, y, w, h, arcade.csscolor.BLACK)


def draw_triangle(x1, y1, x2, y2, x3, y3):
    """draws a triangle"""
    arcade.draw_triangle_outline(x1, y1, x2, y2, x3, y3, arcade.csscolor.BLACK)


def draw_pattern(x, y):
    """draws circle, rectangle, triangle pattern"""
    draw_circle(300 + x, 300 + y, 50)
    draw_rectangle(300 + x, 300 + y, 50, 50)
    draw_triangle(300 + x, 307 + y, 305 + x, 295 + y, 295 + x, 295 + y)


# setup

arcade.open_window(600, 600, "Test")
arcade.set_background_color(arcade.csscolor.WHITE)
arcade.start_render()


# creating pattern

draw_pattern(0, 0)
draw_pattern(50, 50)
draw_pattern(-50, -50)
draw_pattern(50, -50)
draw_pattern(-50, 50)
draw_pattern(0, 100)
draw_pattern(100, 0)
draw_pattern(0, -100)
draw_pattern(-100, 0)
draw_pattern(100, 50)
draw_pattern(50, 100)
draw_pattern(-50, 100)
draw_pattern(50, -100)
draw_pattern(-50, -100)
draw_pattern(-100, 50)
draw_pattern(-100, -50)
draw_pattern(100, -50)
draw_circle(300, 300, 30)


# conclusion

arcade.finish_render()
arcade.run()
