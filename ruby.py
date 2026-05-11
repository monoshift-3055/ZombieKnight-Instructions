import random

import pygame

from helpers import load_frames, handle_portal_collision, apply_motion, RUBY_FRAMES
from settings import WINDOW_WIDTH, vector


class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self, platform_group, portal_group):
        """Initialize the ruby"""
        super().__init__()

        #Set constant variables
        # Gravity
        # TODO: assign 3 to self.VERTICAL_ACCELERATION
        self.VERTICAL_ACCELERATION = 3
        # TODO: assign 5 to self.HORIZONTAL_VELOCITY
        self.HORIZONTAL_VELOCITY = 5

        #Animation frames
        # TODO: assign load_frames() to self.ruby_sprites with these 3 arguments
        self.ruby_sprites = load_frames("images/ruby",RUBY_FRAMES,(64, 64))
        #  1: "images/ruby"
        #  2: RUBY_FRAMES
        #  3: (64, 64)

        #Load image and get rect
        # TODO: assign 0 to self.current_sprite
        self.current_sprite = 0
        # TODO: assign self.ruby_sprites[self.current_sprite] to self.image
        self.image = self.ruby_sprites[self.current_sprite]
        # TODO: assign self.image.get_rect() to self.rect
        self.rect = self.image.get_rect()
        # TODO: assign (WINDOW_WIDTH // 2, 100) to self.rect.bottomleft
        self.rect.bottomleft = (WINDOW_WIDTH // 2, 100)


        #Attach sprite groups
        # TODO: assign platform_group to self.platform_group
        self.platform_group = platform_group
        # TODO: assign portal_group to self.portal_group
        self.portal_group = portal_group


        #Load sounds
        # TODO: assign pygame.mixer.Sound() to self.portal_sound with this 1 argument
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")
        # 1: "sounds/portal_sound.wav"

        #Kinematic vectors
        # TODO: assign vector() to self.position with these 2 arguments
        self.position = vector(self.rect.x,self.rect.y)
        #  1: self.rect.x
        #  2: self.rect.y

        # TODO: assign vector() to self.velocity with these 2 arguments
        self.velocity = vector(random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]),0)
        #  1: random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY])
        #  2: 0

        # TODO: assign vector() to self.acceleration with these 2 arguments
        self.acceleration = vector(0,self.VERTICAL_ACCELERATION)
        #  1: 0
        #  2: self.VERTICAL_ACCELERATION


    def update(self):
        """Update the ruby"""
        # TODO: call self.animate() with these 2 arguments
        self.animate(self.ruby_sprites,0.25)
        #  1: self.ruby_sprites
        #  2: 0.25

        # TODO: call self.move()
        self.move()
        # TODO: call self.check_collisions()
        self.check_collisions()


    def move(self):
        """Move the ruby"""
        # TODO: call apply_motion() with 1 argument
        apply_motion(self)
        #  1: self


    # noinspection PyTypeChecker
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        #Collision check between ruby and platforms when falling
        # TODO: assign pygame.sprite.spritecollide() to collided_platforms with these 3 arguments
        collided_platforms = pygame.sprite.spritecollide(self,self.platform_group,False)
        #  1: self
        #  2: self.platform_group
        #  3: False

        # TODO: if collided_platforms:
        if collided_platforms:
            # TODO: assign collided_platforms[0].rect.top + 1 to self.position.y
            self.position.y = collided_platforms[0].rect.top + 1
            # TODO: assign 0 to self.velocity.y
            self.velocity.y = 0

        # Collision check for portals
        # TODO: call handle_portal_collision() with 1 argument
        handle_portal_collision(self)
        #  1: self


    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        # TODO: if self.current_sprite < len(sprite_list) -1:
        if self.current_sprite < len(sprite_list) - 1:
            # TODO: add speed to self.current_sprite
            self.current_sprite += speed
        # TODO: else:
        else:
            # TODO: assign 0 to self.current_sprite
            self.current_sprite = 0
        # TODO: assign sprite_list[int(self.current_sprite)] to self.image
            self.image = self.ruby_sprites[self.current_sprite]
