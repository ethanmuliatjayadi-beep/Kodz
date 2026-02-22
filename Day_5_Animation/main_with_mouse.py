import arcade

class myGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # VARIABLE DARI BOLA
        self.position_x = 50 + 10
        self.position_y = 50

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.position_x, self.position_y, 10, arcade.color.WHITE)

    def on_mouse_motion(self, x, y, dx, dy):
        self.position_x = x
        self.position_y = y
def main():
    window = myGame(800, 600, "My Game")
    arcade.run()

main()