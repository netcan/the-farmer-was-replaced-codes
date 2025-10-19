from core import do_harvest, reset_farm_state, scan_farm
from plant_pumpkin import plant_pumpkin


def pumpkin():
    # Continuously scan the farm planting pumpkins and harvesting when ready.
    while True:
        scan_farm(plant_pumpkin())
        if can_harvest():
            do_harvest()


def run():
    reset_farm_state()
    pumpkin()


run()
