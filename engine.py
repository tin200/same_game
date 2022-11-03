def _index_to_delete(pos_of_touched, before_checked, blocks_dict):
    """
    :param pos_of_touched:
    :param before_checked:
    :return: lista di indici da rimuovere dal gruppo sprite
    """

    alone_counter = 0
    global terms

    if pos_of_touched in terms:
        return

    # check left
    if before_checked != "left":
        """
        se presente il blocco chiamo la funzione in modo ricorsivo, altrimenti aggiungo il contatore
        """

        try:
            left_block_color = blocks_dict[(pos_of_touched[0] - 50, pos_of_touched[1])]
            if left_block_color == blocks_dict[pos_of_touched]:  # se hanno lo stesso colore
                _index_to_delete((pos_of_touched[0] - 50, pos_of_touched[1]), "right", blocks_dict)
            else:
               alone_counter += 1
               terms.append(pos_of_touched)

        except:
            pass

    # check right
    if before_checked != "right":
        try:
            right_block_color = blocks_dict[(pos_of_touched[0] + 50, pos_of_touched[1])]
            if right_block_color == blocks_dict[pos_of_touched]:  # se hanno lo stesso colore
                _index_to_delete((pos_of_touched[0] + 50, pos_of_touched[1]), "left", blocks_dict)
            else:
                alone_counter += 1
                terms.append(pos_of_touched)

        except:
            pass

    # check up
    if before_checked != "up":
        try:
            up_block_color = blocks_dict[(pos_of_touched[0], pos_of_touched[1] + 50)]
            if up_block_color == blocks_dict[pos_of_touched]:  # se hanno lo stesso colore
                _index_to_delete((pos_of_touched[0], pos_of_touched[1] + 50), "down", blocks_dict)
            else:
                alone_counter += 1
                terms.append(pos_of_touched)

        except:
            pass

    # check down
    if before_checked != "down":
        try:
            down_block_color = blocks_dict[(pos_of_touched[0], pos_of_touched[1] - 50)]
            if down_block_color == blocks_dict[pos_of_touched]:  # se hanno lo stesso colore
                _index_to_delete((pos_of_touched[0], pos_of_touched[1] - 50), "up", blocks_dict)
            else:
                alone_counter += 1
                terms.append(pos_of_touched)

        except:
            pass

    if alone_counter == 3:
        terms.append(pos_of_touched)

    return list(set(terms))


def index_to_delete(pos_of_touched, before_checked, blocks_dict):
    global terms
    terms = []
    return _index_to_delete(pos_of_touched, before_checked, blocks_dict)

