import arcade

class myGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # VARIABLE DARI BOLA
        self.ball_x = 50 + 10
        self.ball_y = 50
        self.ball_speed = 5
        self.ball1_x = 400
        self.ball1_y = 400
        self.ball1_speed = 5

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(self.ball1_x, self.ball1_y, 10, arcade.color.WHITE)

    def on_update(self, delta_time: float):
        self.ball_x += self.ball_speed
        if self.ball_x > self.width or self.ball_x < 0: # Jika bola melebihi lebar atau melebihi 0
            self.ball_speed *= -1 # Maka bola akan mundur

        self.ball1_x += self.ball1_speed
        if self.ball1_x > self.width or self.ball1_x < 0: # Jika bola melebihi lebar atau melebihi 0
            self.ball1_speed *= -1 # Maka bola akan mundur
def main():
    window = myGame(800, 600, "My Game")
    arcade.run()

main()