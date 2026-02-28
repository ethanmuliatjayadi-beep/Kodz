import arcade


class Player(arcade.Sprite):
    """
    Player sprite class for 2D platformer.
    Manages player state and processes input signals without direct movement.
    """
    
    def __init__(self, center_x: float = 100, center_y: float = 100):
        """
        Initialize the player sprite.
        
        Args:
            center_x: Initial X position
            center_y: Initial Y position
        """
        # Create a simple colored rectangle sprite
        super().__init__(arcade.SpriteSolidColor(40, 60, arcade.color.BLUE))
        
        # Position
        self.center_x = center_x
        self.center_y = center_y
        
        # Movement parameters
        self.movement_speed = 8.0
        self.jump_height = 15.0
        
        # State variables
        self.facing_left = False
        self.is_jumping = False
        self.is_grounded = False
        
        # Input states
        self.move_left_pressed = False
        self.move_right_pressed = False
        self.jump_pressed = False
        
        from PIL import Image, ImageDraw
        import numpy as np
        
        # Create a simple image
        image = Image.new('RGBA', (int(self.width), int(self.height)), (0, 0, 255, 255))
        self.texture = arcade.Texture.create_from_image(image)
        
    def move_left(self):
        """
        Signal to move left. Updates velocity vector, not position.
        """
        self.move_left_pressed = True
        self.facing_left = True
        
    def move_right(self):
        """
        Signal to move right. Updates velocity vector, not position.
        """
        self.move_right_pressed = True
        self.facing_left = False
        
    def stop_move_left(self):
        """
        Stop left movement signal.
        """
        self.move_left_pressed = False
        
    def stop_move_right(self):
        """
        Stop right movement signal.
        """
        self.move_right_pressed = False
        
    def jump(self):
        """
        Signal to jump. Only processes if grounded.
        """
        if self.is_grounded and not self.jump_pressed:
            self.jump_pressed = True
            self.is_jumping = True
            
    def stop_jump(self):
        """
        Stop jump signal.
        """
        self.jump_pressed = False
        
    def update_state(self, is_grounded: bool):
        """
        Update player state based on physics feedback.
        
        Args:
            is_grounded: Whether player is currently on a platform
        """
        self.is_grounded = is_grounded
        
        # Reset jumping state when landed
        if self.is_grounded and self.change_y == 0:
            self.is_jumping = False
            
    def process_input(self):
        """
        Process current input states and update velocity vectors.
        This is called by the physics engine to apply movement.
        """
        # Horizontal movement
        if self.move_left_pressed:
            self.change_x = -self.movement_speed
        elif self.move_right_pressed:
            self.change_x = self.movement_speed
        else:
            # No horizontal input, let friction handle deceleration
            pass
            
        # Jump input (handled by physics engine)
        if self.jump_pressed and self.is_grounded:
            return True  # Signal to jump
            
        return False  # No jump requested
        
    def get_movement_speed(self) -> float:
        """
        Get the current movement speed.
        
        Returns:
            Movement speed value
        """
        return self.movement_speed
        
    def get_jump_height(self) -> float:
        """
        Get the current jump height.
        
        Returns:
            Jump height value
        """
        return self.jump_height
        
    def set_movement_speed(self, speed: float):
        """
        Set the movement speed.
        
        Args:
            speed: New movement speed value
        """
        self.movement_speed = speed
        
    def set_jump_height(self, height: float):
        """
        Set the jump height.
        
        Args:
            height: New jump height value
        """
        self.jump_height = height