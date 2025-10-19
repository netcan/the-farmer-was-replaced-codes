from core import do_harvest, reset_farm_state


def make_maze(substance=None):
    # Create a maze using the weird substance.
    if substance == None:
        substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)


def play_maze():
    # Repeatedly generate mazes, search for treasure, and harvest it.
    def dfs_find_treasure():
        current_x, current_y = get_pos_x(), get_pos_y()

        if get_entity_type() == Entities.Treasure:
            return True

        visited[(current_x, current_y)] = True

        directions = []

        tx, ty = measure()
        if tx - current_x > 0:
            directions.append(East)
        else:
            directions.append(West)

        if ty - current_y > 0:
            directions.append(North)
        else:
            directions.append(South)

        for direction in [East, West, North, South]:
            if direction not in directions:
                directions.append(direction)

        for direction in directions:
            if can_move(direction):
                next_x, next_y = current_x, current_y
                if direction == East:
                    next_x += 1
                elif direction == West:
                    next_x -= 1
                elif direction == North:
                    next_y += 1
                elif direction == South:
                    next_y -= 1

                if (next_x, next_y) not in visited:
                    move(direction)
                    if dfs_find_treasure():
                        return True
                    if direction == East:
                        move(West)
                    elif direction == West:
                        move(East)
                    elif direction == North:
                        move(South)
                    elif direction == South:
                        move(North)

        return False

    substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
    while True:
        make_maze(substance)
        visited = {}
        dfs_find_treasure()
        if get_entity_type() == Entities.Treasure:
            do_harvest()
        clear()


def run():
    reset_farm_state()
    play_maze()


run()
