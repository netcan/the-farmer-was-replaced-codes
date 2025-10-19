change_hat(Hats.Purple_Hat)
clear()

def do_plant(type):
    need_soil = [Entities.Carrot, Entities.Sunflower, Entities.Pumpkin, Entities.Cactus]
    if type in need_soil:
        if get_ground_type() != Grounds.Soil:
            till()
    else:
        if get_ground_type() == Grounds.Soil:
            till()

    plant(type)
    if get_water() < 0.5 and num_items(Items.Water) > 0:
        use_item(Items.Water)

    # if num_items(Items.Fertilizer) > 0:
    #     use_item(Items.Fertilizer)

def do_harvest():
    # if get_entity_type() == Entities.Sunflower:
    #     if measure() > 14:
    #         return

    harvest()

def move_dir_n(dir, n):
    movable = True
    for i in range(n):
        if not movable:
            break
        movable = movable and move(dir)
    return movable

def move_to(x, y, shortest=True):
    N = get_world_size()
    cx, cy = get_pos_x(), get_pos_y()
    if shortest:
        dx = ((x - cx + N // 2) % N) - N // 2
        dy = ((y - cy + N // 2) % N) - N // 2
    else:
        dx = x - cx
        dy = y - cy
    movable = True
    for d, dir_pos, dir_neg in [(dx, East, West), (dy, North, South)]:
        if d > 0:
            movable = movable and move_dir_n(dir_pos, d)
        elif d < 0:
            movable = movable and move_dir_n(dir_neg, -d)
    return movable

def scan_farm(func):
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

def fork_join(f, maxN = max_drones()):
    drone_handle = []
    for id in range(maxN - 1):
        def f_warpper(id_ = id):
            f(id_)
        drone_handle.append(spawn_drone(f_warpper))
    f(maxN - 1)
    for handle in drone_handle:
        if handle:
            wait_for(handle)

def spawn_by_column(f, maxN = max_drones()):
    N = get_world_size()
    perN = (N + maxN - 1) // maxN
    quick_print("perN", perN)

    def run_column(id):
        if id * perN >= N:
            return
        exited = False
        while not exited:
            for x in range(id * perN, min((id + 1) * perN, N)):
                for y in range(N):
                    move_to(x, y)
                    exited = f()
                    if exited:
                        break
                if exited:
                    break
    fork_join(run_column, maxN)

def spawn_by_row(f, maxN = max_drones()):
    N = get_world_size()
    perN = (N + maxN - 1) // maxN
    quick_print("perN", perN)

    def run_row(id):
        if id * perN >= N:
            return
        exited = False
        while not exited:
            for x in range(id * perN, min((id + 1) * perN, N)):
                for y in range(N):
                    move_to(y, x)
                    exited = f()
                    if exited:
                        break
                if exited:
                    break
    fork_join(run_row, maxN)

def shuffle_list(a_list):
    n = len(a_list)
    for i in range(n - 1, 0, -1):
        j = random() * (i + 1) // 1
        a_list[i], a_list[j] = a_list[j], a_list[i]
    return a_list

###############################################################################

def plant_by_column(plant_type = [Entities.Carrot, Entities.Tree, Entities.Grass]):
    def f():
        if can_harvest():
            do_harvest()
            plant_ty = plant_type[get_pos_x() % len(plant_type)]
            if plant_ty == Entities.Tree and get_pos_y() % 2 == 1:
                plant_ty = Entities.Bush
            do_plant(plant_ty)
        return num_items(Items.Hay) >= 2000000000
    return f

def plant_pumpkin():
    pumpkin_pos = []
    minx = get_world_size()
    maxx = 0
    miny = get_world_size()
    maxy = 0

    def do_plant_pumpkin():
        global pumpkin_pos
        global minx
        global miny
        global maxx
        global maxy
        if get_entity_type() != Entities.Pumpkin:
            do_plant(Entities.Pumpkin)

        pos = (get_pos_x(), get_pos_y())
        # minx = min(minx, pos[0])
        # maxx = max(maxx, pos[0])
        # miny = min(miny, pos[1])
        # maxy = max(maxy, pos[1])

        if can_harvest():
            if pos not in pumpkin_pos:
                pumpkin_pos.append(pos)
        else:
            if pos in pumpkin_pos:
                pumpkin_pos.remove(pos)
        quick_print("len = ", len(pumpkin_pos))
        # return len(pumpkin_pos) == max((maxx - minx + 1) * (maxy - miny + 1), get_world_size())
        return len(pumpkin_pos) == 36

    return do_plant_pumpkin


def plant_cactus():
    N = get_world_size()
    perN = (N + max_drones() - 1) // max_drones()
    # while num_items(Items.Cactus) < 33554432:
    while True:
        def sort_by_row(id):
            for x in range(id * perN, min((id + 1) * perN, N)):
                for y in range(N):
                    move_to(y, x)
                    do_plant(Entities.Cactus)

                for i in range(N - 1):
                    swapped = False
                    for j in range(N - 1 - i):
                        move_to(j, x)
                        if measure() > measure(East):
                            swap(East)
                            swapped = True
                    if not swapped:
                        break

        fork_join(sort_by_row)

        def sort_by_col(id):
            for x in range(id * perN, min((id + 1) * perN, N)):
                for i in range(N - 1):
                    swapped = False
                    for j in range(N - 1 - i):
                        move_to(x, j)
                        if measure() > measure(North):
                            swap(North)
                            swapped = True
                    if not swapped:
                        break

        fork_join(sort_by_col)

        do_harvest()


def snake_coords(n):
    path = []
    # 第一行：从左到右，全覆盖
    for col in range(n):
        path.append((0, col))
    if n == 1:
        return path
    # 子网格部分
    current_row = 1
    direction = -1  # 开始向左
    extend_row = n - 2
    if n % 2 == 0:
        extend_row = n - 1
    while current_row < n:
        if direction == 1:  # 向右
            start_c = 1
            if (current_row == n-1 and n % 2 == 1):
                start_c = 0
            cols = range(start_c, n)
        else:  # 向左
            if current_row == extend_row:
                cols = range(n-1, -1, -1)
            else:
                cols = range(n-1, 0, -1)
        for col in cols:
            path.append((current_row, col))
        # 如果是偶数n的最后一行，向左扩展到0后，向上填充第0列
        if current_row == n-1 and n % 2 == 0:
            for r in range(n-2, 0, -1):
                path.append((r, 0))
            break
        current_row += 1
        direction = -direction
    return path

def play_dino():
    N = get_world_size()
    coords = snake_coords(N)
    quick_print("coords = ", coords)
    idx = 1
    change_hat(Hats.Dinosaur_Hat)
    while True:
        # if get_entity_type() == Entities.Apple:
        #     x, y = measure()
        #     for retry in range(30):
        #         movable = move_to(x, y, False)
        #         if movable:
        #             break

        #         rx = N * random() // 1
        #         ry = N * random() // 1
        #         move_to(rx, ry, False)

        #         for (rx, ry) in [(get_pos_x(), N - 1), (get_pos_x(), 0), (0, get_pos_y()), (N - 1, get_pos_y())]:
        #             if move_to(rx, ry, False):
        #                 break

        #     if not movable:
        #         change_hat(Hats.Purple_Hat)
        #         change_hat(Hats.Dinosaur_Hat)


    #     if can_harvest():
    #         do_harvest()

        tx, ty = coords[idx]
        idx += 1
        moveable = move_to(tx, ty, False)
        if not moveable:
            change_hat(Hats.Purple_Hat)
            change_hat(Hats.Dinosaur_Hat)

        if idx >= len(coords):
            idx = 0

def play_companion():
    random_plant = [Entities.Carrot, Entities.Sunflower, Entities.Grass, Entities.Bush, Entities.Tree]
    while True:
        if can_harvest():
            do_harvest()

        random_ty = random_plant[random() * len(random_plant) // 1]
        quick_print("random_ty = ", random_ty)
        do_plant(random_ty)

        while get_companion() != None:
            next_ty, (nx, ny) = get_companion()
            quick_print("next_ty = ", random_ty)
            quick_print("nx = ", nx)
            quick_print("ny = ", ny)
            move_to(nx, ny)
            if can_harvest():
                do_harvest()
            do_plant(next_ty)

def plant_tree():
    if can_harvest():
        do_harvest()

    if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0:
        do_plant(Entities.Tree)
    else:
        do_plant(Entities.Grass)

    if num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)

def make_maze(substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)):
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)

################################################################################
# set_world_size(5)
# make_maze()
################################################################################


def play_maze():
    maze_visited_coords = {}
    def dfs_find_treasure():
        current_x, current_y = get_pos_x(), get_pos_y()

        if get_entity_type() == Entities.Treasure:
            return True

        global maze_visited_coords
        maze_visited_coords[(current_x, current_y)] = True

        ALL_DIRS = []

        tx, ty = measure()
        if tx - current_x > 0:
            ALL_DIRS.append(East)
        else:
            ALL_DIRS.append(West)

        if ty - current_y > 0:
            ALL_DIRS.append(North)
        else:
            ALL_DIRS.append(South)

        for dir in [East, West, North, South]:
            if dir not in ALL_DIRS:
                ALL_DIRS.append(dir)

        for direction in ALL_DIRS:
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

                if (next_x, next_y) not in maze_visited_coords:
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
    # set_world_size()
    # make_maze(substance)
    while True:
        make_maze(substance)
        maze_visited_coords = {}
        dfs_find_treasure()
        if get_entity_type() == Entities.Treasure:
            # use_item(Items.Weird_Substance, substance)
            do_harvest()
        clear()

def pumpkin():
    while True:
        scan_farm(plant_pumpkin())
        if can_harvest():
            do_harvest()

def pumpkin_parallel():
    while True:
        spawn_by_column(plant_pumpkin())
        if can_harvest():
            do_harvest()

# scan_farm(plant_by_column())
# spawn_by_column(plant_by_column([Entities.Grass]))
# spawn_by_column(plant_by_column())
# pumpkin()
# pumpkin_parallel()

# scan_farm(plant_tree)
# spawn_by_column(plant_tree)
# plant_cactus()
play_dino()
# play_companion()

# play_maze()