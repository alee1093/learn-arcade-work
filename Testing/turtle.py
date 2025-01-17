import arcade
arcade.open_window(600,600,"Tortal")
arcade.set_background_color(arcade.csscolor.LIGHT_GOLDENROD_YELLOW)

arcade.start_render()
arcade.draw_polygon_filled(((210,320),
                            (240,290),
                            (190,220),
                            (220,260),
                            (230,220)
                            ),
                           (0,204,68))
arcade.draw_polygon_filled(((330,320),
                            (360,290),
                            (310,220),
                            (340,260),
                            (350,220)
                            ),
                           (0,204,68))
arcade.draw_ellipse_filled(300,300,250,130,(153,204,0))
arcade.draw_ellipse_filled(165,290,90,60,(0,204,68))
arcade.draw_triangle_filled(420,320,420,280,450,300,(0,204,68))
arcade.draw_polygon_filled(((240,300),
                            (270,270),
                            (220,200),
                            (250,240),
                            (260,200)
                            ),
                           (0,204,68))
arcade.draw_polygon_filled(((360,300),
                            (390,270),
                            (340,200),
                            (370,240),
                            (380,200)
                            ),
                           (0,204,68))
arcade.draw_ellipse_filled(300,320,270,130,(32,96,32))
arcade.draw_ellipse_filled(300,340,200,110,(51,153,51))
arcade.draw_ellipse_filled(300,360,100,70,(32,96,32))
arcade.draw_ellipse_filled(340,373,35,25,(255,255,255),0,180)
arcade.draw_ellipse_filled(325,365,40,35,(32,96,32),0,180)
arcade.draw_ellipse_filled(420,330,20,30,(255,255,255),0,180)
arcade.draw_ellipse_filled(415,330,25,40,(32,96,32),0,180)
arcade.draw_circle_filled(center_x=425,
                          center_y=338,
                          radius=3,
                          color=(255,255,255))
arcade.draw_ellipse_filled(345,347,15,7,(255,255,255),0,180)
arcade.draw_circle_filled(166,295,7,arcade.csscolor.BLACK)
arcade.draw_circle_filled(167,296,3,arcade.csscolor.WHITE)
arcade.draw_text("Turtellini the Turtle",
                170, 100,
                 arcade.color.PISTACHIO, 24)
arcade.finish_render()
arcade.run()