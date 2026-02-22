import arcade
import time

class myGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # VARIABLE DARI BOLA
        self.position_x = 50 + 10
        self.position_y = 50
        self.change_x = 0
        self.change_y = 0
        self.movement_speed = 5
        self.after_press_x = 0
        self.after_press_y = 0
        self.after_press_time = 0
        self.after_press_duration = 0.3
    
    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.position_x, self.position_y, 10, arcade.color.WHITE)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.change_x = -self.movement_speed
        elif key == arcade.key.D:
            self.change_x = self.movement_speed
        elif key == arcade.key.W:
            self.change_y = self.movement_speed
        elif key == arcade.key.S:
            self.change_y = -self.movement_speed
        elif key == arcade.key.P:
            self.movement_speed =10
        elif key == arcade.key.O:
            self.movement_speed = 3
    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.after_press_x = self.change_x  # save direction before stopping
            self.after_press_time = time.time()
            self.change_x = 0
        elif key == arcade.key.W or         key == arcade.key.S:
            self.after_press_y = self.change_y  # save direction before stopping
            self.after_press_time = time.time()
            self.change_y = 0
        elif key == arcade.key.P or key == arcade.key.O:
            self.movement_speed = 5
    def on_update(self, delta_time: float):
        # Normal movement
        self.position_x += self.change_x
        self.position_y += self.change_y

        # After-release momentum (slides for after_press_duration seconds)
        if time.time() - self.after_press_time < self.after_press_duration:
            self.position_x += self.after_press_x
            self.position_y += self.after_press_y
        else:
            self.after_press_x = 0
            self.after_press_y = 0
def main():
    window = myGame(800, 600, "My Game")
    arcade.run()

main()