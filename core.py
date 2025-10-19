def do_plant(entity_type):
    # Plant an entity after ensuring the ground matches its requirements.
    need_soil = [Entities.Carrot, Entities.Sunflower, Entities.Pumpkin, Entities.Cactus]
    if entity_type in need_soil:
        if get_ground_type() != Grounds.Soil:
            till()
    else:
        if get_ground_type() == Grounds.Soil:
            till()

    plant(entity_type)
    if get_water() < 0.5 and num_items(Items.Water) > 0:
        use_item(Items.Water)


def do_harvest():
    # Harvest the entity under the drone.
    harvest()


def move_dir_n(direction, steps):
    # Attempt to move in one direction up to the given number of steps.
    movable = True
    for _ in range(steps):
        if not movable:
            break
        movable = movable and move(direction)
    return movable


def move_to(x, y, shortest=True):
    # Move to a target coordinate, optionally using toroidal shortest paths.
    size = get_world_size()
    current_x, current_y = get_pos_x(), get_pos_y()
    if shortest:
        dx = ((x - current_x + size // 2) % size) - size // 2
        dy = ((y - current_y + size // 2) % size) - size // 2
    else:
        dx = x - current_x
        dy = y - current_y

    movable = True
    for delta, positive_dir, negative_dir in [(dx, East, West), (dy, North, South)]:
        if delta > 0:
            movable = movable and move_dir_n(positive_dir, delta)
        elif delta < 0:
            movable = movable and move_dir_n(negative_dir, -delta)
    return movable


def fork_join(func, max_workers=max_drones()):
    # Run a function across multiple drones and wait for completion.
    drone_handles = []
    for worker_id in range(max_workers - 1):
        def wrapper(idx=worker_id):
            func(idx)
        drone_handles.append(spawn_drone(wrapper))

    func(max_workers - 1)
    for handle in drone_handles:
        if handle:
            wait_for(handle)


def reset_farm_state():
    # Reset hat and clear the farm before running a scenario.
    change_hat(Hats.Purple_Hat)
    clear()


def scan_farm(func):
    # Traverse the entire farm, invoking the callback on each tile.
    exited = False
    while not exited:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                exited = func()
                move(North)
                if exited:
                    break
            move(East)
            if exited:
                break


def spawn_by_column(callback, max_workers=max_drones()):
    # Spawn drones to process the farm column by column.
    size = get_world_size()
    per_worker = (size + max_workers - 1) // max_workers
    quick_print("perN", per_worker)

    def run_column(worker_id):
        if worker_id * per_worker >= size:
            return
        exited = False
        while not exited:
            for x in range(worker_id * per_worker, min((worker_id + 1) * per_worker, size)):
                for y in range(size):
                    move_to(x, y)
                    exited = callback()
                    if exited:
                        break
                if exited:
                    break

    fork_join(run_column, max_workers)
