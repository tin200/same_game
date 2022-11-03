import sys
import pygame
from set import draw_grill, return_dict_blocks_color, return_grid, update_block_dict, update_blocks_dict_after_sprite_elimination, return_dict_with_the_second_element_higher
from engine import index_to_delete

SIZE = (700, 601)
BLACK = (0, 0, 0)
BLU = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode(SIZE)

dict_blocks = return_dict_blocks_color(return_grid())

blocks = pygame.sprite.Group()
blocks = draw_grill(blocks, dict_blocks)
point = 0

go = True
while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for block in blocks:
                if block.rect.collidepoint(event.pos):
                    to_delete = index_to_delete((block.rect.x, block.rect.y), "", dict_blocks)
                    point += len(to_delete)
                    for block_ in blocks:
                        if (block_.rect.x, block_.rect.y) in to_delete:
                            blocks.remove(block_)
                    blocks.remove(block)
                    print(return_dict_with_the_second_element_higher(to_delete))
                    print(update_blocks_dict_after_sprite_elimination(blocks, dict_blocks))

    screen.fill(BLACK)
    blocks.draw(screen)
    pygame.display.flip()
