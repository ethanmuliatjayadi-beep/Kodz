import arcade
from typing import List


class PlatformerPhysics:
    """
    Custom physics controller for 2D platformer games.
    Handles gravity, movement, collisions, and jump mechanics.
    """
    
    def __init__(self, player: arcade.Sprite, platforms: List[arcade.Sprite],
                 gravity: float = 1.0, terminal_velocity: float = 15.0):
        """
        Initialize the physics engine.
        
        Args:
            player: The player sprite to control
            platforms: List of platform sprites for collision detection
            gravity: Downward acceleration applied each frame
            terminal_velocity: Maximum falling speed
        """
        self.player = player
        self.platforms = platforms
        self.gravity = gravity
        self.terminal_velocity = terminal_velocity
        
        # Movement constants
        self.acceleration = 0.5
        self.friction = 0.7
        self.jump_impulse = -15.0
        
        # State tracking
        self.is_grounded = False
        
    def update(self):
        """
        Update physics for one frame.
        Applies gravity, handles movement, and processes collisions.
        """
        # Apply gravity
        self.player.change_y -= self.gravity
        
        # Enforce terminal velocity
        if self.player.change_y < -self.terminal_velocity:
            self.player.change_y = -self.terminal_velocity
            
        # Apply horizontal friction
        self.player.change_x *= self.friction
        
        # Update position
        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y
        
        # Check collisions
        self._check_collisions()
        
    def _check_collisions(self):
        """
        Check and resolve collisions with platforms.
        """
        # Reset grounded state
        self.is_grounded = False
        
        # Check collision with each platform
        for platform in self.platforms:
            if arcade.check_for_collision(self.player, platform):
                self._resolve_collision(platform)
                
    def _resolve_collision(self, platform: arcade.Sprite):
        """
        Resolve collision between player and a specific platform.
        """
        # Get collision boundaries
        player_left = self.player.left
        player_right = self.player.right
        player_bottom = self.player.bottom
        player_top = self.player.top
        
        platform_left = platform.left
        platform_right = platform.right
        platform_bottom = platform.bottom
        platform_top = platform.top
        
        # Calculate overlap amounts
        overlap_left = player_right - platform_left
        overlap_right = platform_right - player_left
        overlap_bottom = player_top - platform_bottom
        overlap_top = platform_right - player_bottom
        
        # Find smallest overlap
        min_overlap = min(overlap_left, overlap_right, overlap_bottom, overlap_top)
        
        # Resolve collision based on smallest overlap
        if min_overlap == overlap_bottom and self.player.change_y <= 0:
            # Landing on top of platform
            self.player.bottom = platform_top
            self.player.change_y = 0
            self.is_grounded = True
            
        elif min_overlap == overlap_top and self.player.change_y > 0:
            # Hitting platform from below
            self.player.top = platform_bottom
            self.player.change_y = 0
            
        elif min_overlap == overlap_left:
            # Hitting platform from right
            self.player.right = platform_left
            self.player.change_x = 0
            
        elif min_overlap == overlap_right:
            # Hitting platform from left
            self.player.left = platform_right
            self.player.change_x = 0
            
    def jump(self):
        """
        Apply jump impulse if player is grounded.
        """
        if self.is_grounded:
            self.player.change_y = self.jump_impulse
            self.is_grounded = False
            
    def move_left(self, speed: float):
        """
        Apply leftward movement.
        
        Args:
            speed: Movement speed multiplier
        """
        self.player.change_x -= self.acceleration * speed
        
    def move_right(self, speed: float):
        """
        Apply rightward movement.
        
        Args:
            speed: Movement speed multiplier
        """
        self.player.change_x += self.acceleration * speed
        
    def is_player_grounded(self) -> bool:
        """
        Check if player is currently grounded.
        
        Returns:
            True if player is on a platform, False otherwise
        """
        return self.is_grounded