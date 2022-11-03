import itertools
import random
from Block import Block


RED = (255, 0, 0)
BLU = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
SILVER = (192, 192, 192)


def return_grid():
    X = [x for x in range(0, 551) if x % 50 == 0]
    Y = [y for y in range(0, 551) if y % 50 == 0]

    grid = list(itertools.product(X, Y))

    return grid


def draw_grill(sprite_group, block_dict):
    grid = return_grid()

    for i in range(0, 144):
        sprite_group.add(Block(block_dict[grid[i]], grid[i]))

    return sprite_group


def return_dict_blocks_color(grid):
    colors = [RED, BLU, GREEN, YELLOW, AQUA]
    blocks_dict = {}
    for pos in grid:
        blocks_dict[pos] = random.choice(colors)

    return blocks_dict


def update_blocks_dict_after_sprite_elimination(sprite_group, blocks_dict):
    """

    :param sprite_group:
    :param blocks_dict:
    :return: restituisce il dizionario dei blocchi dopo l'eliminazione di alcuni elementi dal gruppo sprite
    """
    to_delete = []
    sprite_group_pos = []
    for sprite in sprite_group:
        sprite_group_pos.append((sprite.rect.x, sprite.rect.y))

    for block in blocks_dict:
        if block not in sprite_group_pos:
            to_delete.append(block)

    for pos in to_delete:
        del blocks_dict[pos]

    return blocks_dict


def return_dict_with_the_second_element_higher(ls):
    """
    :param ls: [a, b] con a e b rappresentanti le coordinate dei blocchi
    :return: dizionario di liste assicurandosi che la coppia [a, b] abbia la b maggiore fissata la a.
    esempio: se ho [1, 2] e [1, 3]. La funzione mi darebbe [1, 3]
    """
    dict_of_sub_list = {}
    sorted(ls)

    for l in ls:
        dict_of_sub_list[l[0]] = l[1]

    for l in ls:
        if dict_of_sub_list[l[0]] < l[1]:
            dict_of_sub_list[l[0]] = l[1]

    return dict_of_sub_list


def update_block_dict(deleted_pos, blocks_dict, sprite_group):
    blocks_dict = update_blocks_dict_after_sprite_elimination(sprite_group, blocks_dict)

    return blocks_dict
