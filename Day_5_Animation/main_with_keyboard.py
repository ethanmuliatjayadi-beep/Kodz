import arcade

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

        self.ball2_x = 400
        self.ball2_y = 400
        self.ball2_movement_speed = 5
    
    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.position_x, self.position_y, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(self.ball2_x, self.ball2_y, 10, arcade.color.WHITE)

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
            self.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.change_y = 0
        elif key == arcade.key.P or key == arcade.key.O:
            self.movement_speed = 5
    def on_update(self, delta_time: float):
        self.position_x += self.change_x
        self.position_y += self.change_y

        self.ball2_x += self.ball2_movement_speed
        if self.ball2_x > self.width or self.ball2_x < 0: # Jika bola melebihi lebar atau melebihi 0
            self.ball2_movement_speed *= -1 # Maka bola akan mundur
def main():
    window = myGame(800, 600, "My Game")
    arcade.run()

main()