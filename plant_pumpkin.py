from core import do_plant


def plant_pumpkin():
    # Return a planting callback that grows pumpkins and tracks completion.
    pumpkin_pos = []

    def do_plant_pumpkin():
        if get_entity_type() != Entities.Pumpkin:
            do_plant(Entities.Pumpkin)

        pos = (get_pos_x(), get_pos_y())

        if can_harvest():
            if pos not in pumpkin_pos:
                pumpkin_pos.append(pos)
        else:
            if pos in pumpkin_pos:
                pumpkin_pos.remove(pos)
        quick_print("len = ", len(pumpkin_pos))
        return len(pumpkin_pos) == 32

    return do_plant_pumpkin
