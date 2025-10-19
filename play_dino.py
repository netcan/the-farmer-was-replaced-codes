from core import move_to, reset_farm_state


def snake_coords(size):
    # Build a snake-like traversal for an NxN grid.
    path = []
    for col in range(size):
        path.append((0, col))
    if size == 1:
        return path

    current_row = 1
    direction = -1
    extend_row = size - 2
    if size % 2 == 0:
        extend_row = size - 1

    while current_row < size:
        if direction == 1:
            start_col = 1
            if current_row == size - 1 and size % 2 == 1:
                start_col = 0
            columns = range(start_col, size)
        else:
            if current_row == extend_row:
                columns = range(size - 1, -1, -1)
            else:
                columns = range(size - 1, 0, -1)

        for col in columns:
            path.append((current_row, col))

        if current_row == size - 1 and size % 2 == 0:
            for row in range(size - 2, 0, -1):
                path.append((row, 0))
            break

        current_row += 1
        direction = -direction

    return path


def play_dino():
    # Patrol the farm in a snake pattern while wearing the dinosaur hat.
    size = get_world_size()
    coords = snake_coords(size)
    quick_print("coords = ", coords)
    idx = 1
    change_hat(Hats.Dinosaur_Hat)
    while True:
        target_x, target_y = coords[idx]
        idx += 1
        moveable = move_to(target_x, target_y, False)
        if not moveable:
            change_hat(Hats.Purple_Hat)
            change_hat(Hats.Dinosaur_Hat)

        if idx >= len(coords):
            idx = 0


def run():
    reset_farm_state()
    play_dino()


run()
