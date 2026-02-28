import arcade
import os

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
SCREEN_TITLE = "Tiled Integration"

PLAYER_SPEED = 5
PLAYER_JUMP = 30
GRAVITY = 1

ENEMY_SPEED = 3

MAP_name = "map_ethan1/day_7/map.tmj"

class myGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.score = 0
        self.item_list = None
        self.enemy_list = None

        self.collect_sound = arcade.load_sound("map_ethan1/day_7/fart.mp3")
        self.jump_sound = arcade.load_sound("map_ethan1/day_7/jump.mp3")
        

    def setup(self):
        tile_map  = arcade.load_tilemap(MAP_name, scaling=3, use_spatial_hash=False)
        self.scene = arcade.Scene.from_tilemap(tile_map)

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 0.8)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.scene.add_sprite("Player", self.player_sprite)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, walls=self.scene["Ground"], gravity_constant=GRAVITY)

        self.player_spawn_x = self.player_sprite.center_x
        self.player_spawn_y = self.player_sprite.center_y

        self.item_list = arcade.SpriteList()
        self.score = 0

        self.enemy_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png", 0.8)
        self.scene.add_sprite("Enemy", self.enemy_sprite)

    def on_draw(self):
        self.clear()
        self.scene.draw()

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 18)
        arcade.draw_text(f"Tekan A/D untuk jalan, SPACE untuk loncat", 10, SCREEN_HEIGHT - 20, arcade.color.WHITE, 18)
    
    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.scene.update_animation(delta_time)

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.item_list)
        for item in hit_list:
            item.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.collect_sound)

    def on_key_press(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W, arcade.key.SPACE):
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP
                arcade.play_sound(self.jump_sound)
        elif key in (arcade.key.LEFT, arcade.key.A):
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.player_sprite.change_x = PLAYER_SPEED
        
    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT, arcade.key.A, arcade.key.D):
            self.player_sprite.change_x = 0
            
    
def main():
    game = myGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
