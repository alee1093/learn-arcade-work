import arcade
arcade.open_window(600, 600, "Sprite_1")
arcade.set_background_color((255, 255, 255))

arcade.start_render()

# units for back
arcade.draw_line(300, 215, 330, 260, arcade.csscolor.BLACK, 5) # right upper arm
arcade.draw_ellipse_outline(315, 350, 20, 35, arcade.csscolor.BLACK, 1, 335) # left hand fill

# head
arcade.draw_circle_filled(300, 300, 50, (255, 219, 172)) # base fill
arcade.draw_circle_outline(300, 300, 50, (241, 194, 125)) # base outline
arcade.draw_ellipse_filled(285, 315, 18, 30, (arcade.csscolor.BLACK)) # left eye
arcade.draw_ellipse_filled(288, 320, 5, 10, (arcade.csscolor.WHITE)) # left eye glimmer1
arcade.draw_ellipse_filled(320, 315, 18, 30, (arcade.csscolor.BLACK)) # right eye
arcade.draw_ellipse_filled(323, 320, 5, 10, (arcade.csscolor.WHITE)) # right eye glimmer1
arcade.draw_rectangle_outline(328, 294, 40, 20, (241, 194, 125 )) # nose: rectangle
arcade.draw_rectangle_filled(313, 294, 30, 19, (255, 219, 172)) # nose: erase rectangle
arcade.draw_ellipse_outline(343, 294.5, 45, 19.5, (241, 194, 125)) # nose: ellipse
arcade.draw_ellipse_filled(342, 294, 45, 19.5, (255, 219, 172)) # nose: erase ellipse
arcade.draw_ellipse_filled(303, 270, 16, 19, (204, 0, 0)) # mouth fill
arcade.draw_ellipse_outline(303.3, 270, 16, 19, arcade.csscolor.BLACK, 2) # mouth outline

# mustache
arcade.draw_ellipse_filled(303.5, 276, 30, 13, arcade.csscolor.GREY, 355)

# hat
arcade.draw_rectangle_filled(255, 375, 75, 90, arcade.csscolor.BLACK, 330) # rectangle base
arcade.draw_arc_filled(232, 414, 70, 10, arcade.csscolor.BLACK, 0, 180, 30) # ellipse overlap
arcade.draw_ellipse_filled(275.5, 334.5, 110, 8, arcade.csscolor.BLACK, 330) # ellipse overlap
arcade.draw_line(245, 320, 307, 355.5, arcade.csscolor.WHITE, 0.3) # hat rim lining

# main body (except for right arm)
arcade.draw_line(300, 250, 300, 200, arcade.csscolor.BLACK, 7) # torso
arcade.draw_line(300, 215, 250, 240, arcade.csscolor.BLACK, 5) # left upper arm
arcade.draw_line(250, 240, 240, 293, arcade.csscolor.BLACK, 3) # left lower arm
arcade.draw_ellipse_filled(245, 310, 20, 40, arcade.csscolor.WHITE, 20) # right hand fill
arcade.draw_ellipse_outline(245, 310, 20, 40, arcade.csscolor.BLACK, 1, 20) # right hand outline
arcade.draw_line(300, 200, 286.5, 165, arcade.csscolor.BLACK, 7) # left leg
arcade.draw_line(300, 200, 315, 168, arcade.csscolor.BLACK, 7) # right leg

# shoes
arcade.draw_rectangle_filled(292.5, 160, 20, 15, arcade.csscolor.BLUE) # left foot rectangle fill
arcade.draw_arc_filled(299.8, 153, 22, 28.5, arcade.csscolor.BLUE, 0, 180) # left foot arc filled
arcade.draw_rectangle_filled(319.5, 165, 20, 15, arcade.csscolor.BLUE) # right foot rectangle fill
arcade.draw_arc_filled(326.8, 158, 22, 28.5, arcade.csscolor.BLUE, 0, 180) # right foot arc filled

arcade.finish_render()

arcade.run()