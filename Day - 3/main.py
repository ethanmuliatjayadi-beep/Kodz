import arcade

arcade.open_window(1200, 720, "Drawing Example")

arcade.set_background_color(arcade.csscolor.ALICE_BLUE)

arcade.start_render()

arcade.draw_lrbt_rectangle_filled(75, 175, 150, 500, color=arcade.csscolor.LIGHT_GRAY)
arcade.draw_lrbt_rectangle_filled(425, 525, 150, 500, color=arcade.csscolor.LIGHT_GRAY)
arcade.draw_lrbt_rectangle_filled(250, 350, 150, 650, color=arcade.csscolor.LIGHT_GRAY)
arcade.draw_triangle_filled(x1=85, x2=125, x3=165, y1=500, y2=600, y3=500, color=arcade.csscolor.RED)
arcade.draw_triangle_filled(x1=435, x2=475, x3=515, y1=500, y2=600, y3=500, color=arcade.csscolor.RED)
arcade.draw_triangle_filled(x1=255, x2=300, x3=345, y1=650, y2=750, y3=650, color=arcade.csscolor.RED)
arcade.draw_lrbt_rectangle_filled(175, 425, 150, 400, color=arcade.csscolor.LIGHT_SLATE_GRAY)
arcade.draw_lrbt_rectangle_filled(250, 350, 150, 325, color=arcade.csscolor.GRAY)
arcade.draw_arc_filled(center_x=300, center_y=325, width=75, height=140 , start_angle=0, end_angle=180,color=arcade.csscolor.GRAY)
arcade.draw_lrbt_rectangle_filled(75, 525, 150, 170, color=arcade.csscolor.GRAY)
arcade.draw_arc_filled(center_x=125, center_y=400, width=75, height=140 , start_angle=0, end_angle=180,color=arcade.csscolor.BLACK)
arcade.draw_arc_filled(center_x=300, center_y=550, width=75, height=140 , start_angle=0, end_angle=180,color=arcade.csscolor.BLACK)
arcade.draw_arc_filled(center_x=475, center_y=400, width=75, height=140 , start_angle=0, end_angle=180,color=arcade.csscolor.BLACK)

arcade.finish_render()
arcade.run()
