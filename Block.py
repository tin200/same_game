import pygame


class Block(pygame.sprite.Sprite):
    width = 50
    height = 50

    def __init__(self,  color, coord):
        pygame.sprite.Sprite.__init__(self)

        self.color = color
        self.image = pygame.Surface([Block.width, Block.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coord
