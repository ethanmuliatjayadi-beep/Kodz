import arcade

class myGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

        self.position_x = 50 + 10
        self.position_y = 50
        self.mouse_x = 50 + 10
        self.mouse_y = 50
        self.delay_speed = 0.1

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.position_x, self.position_y, 10, arcade.color.WHITE)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y

    def on_update(self, delta_time: float):
        self.position_x += (self.mouse_x - self.position_x) * self.delay_speed
        self.position_y += (self.mouse_y - self.position_y) * self.delay_speed

def main():
    window = myGame(800, 600, "My Game")
    arcade.run()

main()