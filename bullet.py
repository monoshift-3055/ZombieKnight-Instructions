import pygame


class Bullet(pygame.sprite.Sprite):
    """A projectile launched by the player"""

    def __init__(self, x, y, bullet_group, player):
        """Initialize the bullet"""
        super().__init__()

        #Set constant variables
        # TODO: assign 20 to self.VELOCITY
        self.VELOCITY = 20
        # TODO: assign 500 to self.RANGE
        self.RANGE = 500

        #Load image and get rect
        # TODO: if player.velocity.x > 0:
        if player.velocity.x > 0:
            # TODO: assign pygame.transform.scale() to self.image with these 2 arguments
            self.image = pygame.transform.scale(pygame.image.load("images/player.slash.png"),(32, 32))
            #  1: pygame.image.load("images/player.slash.png")
            #  2: (32, 32)
        # TODO: else:
        else:
            # TODO: assign pygame.transform.scale() to self.image with these 3 arguments
            self.image = pygame.transform.scale(pygame.transform.flip(pygame.image.load("images/player/slash.png"),True,False)
            #  1: pygame.transform.flip(pygame.image.load("images/player/slash.png")
            #  2: True
            #  3: False
            # TODO: assign -1 * self.VELOCITY to self.VELOCITY
            self.VELOCITY = -1 * self.VELOCITY

        # TODO: assign self.image.get_rect() to self.rect
            self.rect = self.image.get_rect()
        # TODO: assign (x, y) to self.rect.center
            self.rect.center = x, y

        # TODO: assign x to self.starting_x
            self.starting_x = x

        # TODO: call bullet_group.add() with this 1 argument
            bullet_group.add(self)
        # 1: self


    def update(self):
        """Update the bullet"""
        # TODO: add self.VELOCITY to self.rect.x
        self.rect.x = self.VELOCITY

        #If the bullet has passed the range, kill it
        # TODO: if abs(self.rect.x - self.starting_x) > self.RANGE:
        if abs(self.rect.x - self.starting_x) > self.RANGE:
            # TODO: self.kill()
            self.kill()
