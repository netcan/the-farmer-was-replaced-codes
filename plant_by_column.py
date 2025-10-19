from core import do_harvest, do_plant, reset_farm_state, scan_farm, spawn_by_column


def plant_by_column(plant_types=None):
    # Create a planting callback that alternates crops by column.
    if plant_types == None:
        plant_types = [Entities.Carrot, Entities.Tree, Entities.Grass]

    def do_planting():
        if can_harvest():
            do_harvest()
            plant_type = plant_types[get_pos_x() % len(plant_types)]
            if plant_type == Entities.Tree and get_pos_y() % 2 == 1:
                plant_type = Entities.Bush
            do_plant(plant_type)
        return num_items(Items.Hay) >= 2000000000

    return do_planting


def run_scan_farm_default():
    reset_farm_state()
    scan_farm(plant_by_column())


def run_spawn_by_column_grass():
    reset_farm_state()
    spawn_by_column(plant_by_column([Entities.Grass]))


def run_spawn_by_column_default():
    reset_farm_state()
    spawn_by_column(plant_by_column())


# run_scan_farm_default()
# run_spawn_by_column_grass()
run_spawn_by_column_default()
