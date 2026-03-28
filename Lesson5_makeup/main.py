import arcade

TITLE = "My Game"
HEIGHT = 600
WIDTH = 800
JUMPPOWER = 10

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.scene = None
        self.player_sprite = None
        self.physics_engine_1 = None
        self.physics_engine_2 = None
        self.box_collision = None

    def setup(self):
        self.scene = arcade.Scene()
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Ground", use_spatial_hash=True)
        self.scene.add_sprite_list("Enemies", use_spatial_hash=True)

        self.player_sprite = arcade.Sprite("player.png", 1)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        self.enemy_sprite = arcade.Sprite("player.png", 1)
        self.enemy_sprite.center_x = 128
        self.enemy_sprite.center_y = 128
        self.scene.add_sprite("Enemies", self.enemy_sprite)

        platform = arcade.Sprite("platform.png", 1)
        platform.center_x = 300
        platform.center_y = 32
        self.scene.add_sprite("Ground", platform)

        self.physics_engine_1 = arcade.PhysicsEnginePlatformer(self.player_sprite, self.scene.get_sprite_list("Ground"))
        self.physics_engine_2 = arcade.PhysicsEnginePlatformer(self.enemy_sprite, self.scene.get_sprite_list("Ground"))
        self.box_collision = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Ground"))

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_update(self, delta_time):
        self.physics_engine_1.update()
        self.physics_engine_2.update()
        self.box_collision.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_sprite.change_x = -5
        elif symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
        elif symbol == arcade.key.SPACE:
            if self.physics_engine_1.can_jump():
                self.player_sprite.change_y = JUMPPOWER
        elif symbol == arcade.key.W:
            if self.physics_engine_2.can_jump():
                self.enemy_sprite.change_y = JUMPPOWER
        elif symbol == arcade.key.A:
            self.enemy_sprite.change_x = -5
        elif symbol == arcade.key.D:
            self.enemy_sprite.change_x = 5

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif symbol == arcade.key.A or symbol == arcade.key.D:
            self.enemy_sprite.change_x = 0

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()