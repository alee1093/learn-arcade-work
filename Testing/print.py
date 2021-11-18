import arcade
arcade.open_window(600,600,"")
arcade.set_background_color(arcade.csscolor.WHITE)


def draw_part():
    x = 0
    y = 0
    for i in range(13):
      arcade.draw_circle_outline(0 + x, 0 + y, 30, arcade.csscolor.BLACK)
      x += 45
      for p in range(i):
            y += i


arcade.start_render()
draw_part()
arcade.finish_render()
arcade.run()