from core import do_harvest, do_plant, reset_farm_state, scan_farm, spawn_by_column


def plant_tree():
    # Plant trees on even tiles and grass elsewhere, fertilizing when possible.
    if can_harvest():
        do_harvest()

    if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
        do_plant(Entities.Tree)
    else:
        do_plant(Entities.Grass)

    if num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)


def run_scan_farm_tree():
    reset_farm_state()
    scan_farm(plant_tree)


def run_spawn_by_column_tree():
    reset_farm_state()
    spawn_by_column(plant_tree)


run_scan_farm_tree()
run_spawn_by_column_tree()
