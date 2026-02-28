import arcade
from player import Player
from physics_engine import PlatformerPhysics


class MyGame(arcade.Window):
    """
    Main game window for the 2D platformer.
    Handles the game loop, input routing, and rendering.
    """
    
    def __init__(self, width: int = 800, height: int = 600, title: str = "2D Platformer"):
        """
        Initialize the game window.
        
        Args:
            width: Window width in pixels
            height: Window height in pixels
            title: Window title
        """
        super().__init__(width, height, title)
        
        # Game state
        self.player = None
        self.physics_engine = None
        self.platforms = None
        
        # Background color
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
    def setup(self):
        """
        Set up the game - initialize sprites and physics engine.
        """
        # Create player sprite
        self.player = Player(center_x=100, center_y=200)
        
        # Create platforms
        self.platforms = arcade.SpriteList()
        
        # Ground platform
        ground = arcade.SpriteSolidColor(800, 40, arcade.color.DARK_GREEN)
        ground.center_x = 400
        ground.center_y = 20
        self.platforms.append(ground)
        
        # Some floating platforms
        platform1 = arcade.SpriteSolidColor(150, 20, arcade.color.DARK_BROWN)
        platform1.center_x = 200
        platform1.center_y = 150
        self.platforms.append(platform1)
        
        platform2 = arcade.SpriteSolidColor(150, 20, arcade.color.DARK_BROWN)
        platform2.center_x = 500
        platform2.center_y = 250
        self.platforms.append(platform2)
        
        platform3 = arcade.SpriteSolidColor(100, 20, arcade.color.DARK_BROWN)
        platform3.center_x = 650
        platform3.center_y = 350
        self.platforms.append(platform3)
        
        # Initialize physics engine
        self.physics_engine = PlatformerPhysics(
            player=self.player,
            platforms=self.platforms,
            gravity=0.8,
            terminal_velocity=12.0
        )
        
    def on_draw(self):
        """
        Render the game scene.
        """
        self.clear()
        
        # Draw platforms
        self.platforms.draw()
        
        # Draw player
        self.player.draw()
        
        # Draw debug info
        self._draw_debug_info()
        
    def _draw_debug_info(self):
        """
        Draw debug information on screen.
        """
        # Create debug text
        debug_text = [
            f"Position: ({self.player.center_x:.1f}, {self.player.center_y:.1f})",
            f"Velocity: ({self.player.change_x:.1f}, {self.player.change_y:.1f})",
            f"Grounded: {self.physics_engine.is_player_grounded()}",
            f"Facing Left: {self.player.facing_left}",
            "",
            "Controls:",
            "WASD or Arrow Keys - Move",
            "Space - Jump",
            "ESC - Exit"
        ]
        
        # Draw text
        y_position = self.height - 30
        for line in debug_text:
            arcade.draw_text(
                line,
                10,
                y_position,
                arcade.color.BLACK,
                12,
                anchor_x="left"
            )
            y_position -= 20
            
    def on_update(self, delta_time: float):
        """
        Update game logic.
        
        Args:
            delta_time: Time since last frame
        """
        # Process player input and update velocity
        should_jump = self.player.process_input()
        
        # Apply jump if requested
        if should_jump:
            self.physics_engine.jump()
            
        # Update physics
        self.physics_engine.update()
        
        # Update player state based on physics feedback
        self.player.update_state(self.physics_engine.is_player_grounded())
        
        # Keep player in bounds
        self._keep_player_in_bounds()
        
    def _keep_player_in_bounds(self):
        """
        Keep the player within screen boundaries.
        """
        # Horizontal bounds
        if self.player.left < 0:
            self.player.left = 0
            self.player.change_x = 0
        elif self.player.right > self.width:
            self.player.right = self.width
            self.player.change_x = 0
            
        # Vertical bounds (allow falling below screen for game over scenario)
        if self.player.bottom < -100:
            # Reset player position if they fall too far
            self.player.center_x = 100
            self.player.center_y = 200
            self.player.change_x = 0
            self.player.change_y = 0
            
    def on_key_press(self, key, modifiers):
        """
        Handle key press events.
        
        Args:
            key: The key that was pressed
            modifiers: Modifier keys (shift, ctrl, etc.)
        """
        # Movement keys
        if key in [arcade.key.LEFT, arcade.key.A]:
            self.player.move_left()
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.player.move_right()
        elif key in [arcade.key.UP, arcade.key.W, arcade.key.SPACE]:
            self.player.jump()
            
        # Exit key
        elif key == arcade.key.ESCAPE:
            self.close()
            
    def on_key_release(self, key, modifiers):
        """
        Handle key release events.
        
        Args:
            key: The key that was released
            modifiers: Modifier keys (shift, ctrl, etc.)
        """
        # Movement keys
        if key in [arcade.key.LEFT, arcade.key.A]:
            self.player.stop_move_left()
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.player.stop_move_right()
        elif key in [arcade.key.UP, arcade.key.W, arcade.key.SPACE]:
            self.player.stop_jump()


def main():
    """
    Main function to run the game.
    """
    game = MyGame()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()