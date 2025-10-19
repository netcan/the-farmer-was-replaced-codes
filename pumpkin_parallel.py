from core import do_harvest, reset_farm_state, spawn_by_column
from plant_pumpkin import plant_pumpkin


def pumpkin_parallel():
    # Parallel pumpkin farming using columns of drones.
    while True:
        spawn_by_column(plant_pumpkin())
        if can_harvest():
            do_harvest()


def run():
    reset_farm_state()
    pumpkin_parallel()


run()
