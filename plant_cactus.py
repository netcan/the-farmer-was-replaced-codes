from core import do_harvest, do_plant, fork_join, move_to, reset_farm_state


def plant_cactus():
    # Continuously grow, sort, and harvest cacti across the farm.
    size = get_world_size()
    per_worker = (size + max_drones() - 1) // max_drones()

    while True:
        def sort_by_row(worker_id):
            for x in range(worker_id * per_worker, min((worker_id + 1) * per_worker, size)):
                for y in range(size):
                    move_to(y, x)
                    do_plant(Entities.Cactus)

                for i in range(size - 1):
                    swapped = False
                    for j in range(size - 1 - i):
                        move_to(j, x)
                        if measure() > measure(East):
                            swap(East)
                            swapped = True
                    if not swapped:
                        break

        fork_join(sort_by_row)

        def sort_by_col(worker_id):
            for x in range(worker_id * per_worker, min((worker_id + 1) * per_worker, size)):
                for i in range(size - 1):
                    swapped = False
                    for j in range(size - 1 - i):
                        move_to(x, j)
                        if measure() > measure(North):
                            swap(North)
                            swapped = True
                    if not swapped:
                        break

        fork_join(sort_by_col)

        do_harvest()


def run():
    reset_farm_state()
    plant_cactus()


run()
