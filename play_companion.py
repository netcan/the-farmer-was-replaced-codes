from core import do_harvest, do_plant, move_to, reset_farm_state


def play_companion():
    # Companion planting loop that follows plant suggestions.
    random_plant = [Entities.Carrot, Entities.Sunflower, Entities.Grass, Entities.Bush, Entities.Tree]
    while True:
        if can_harvest():
            do_harvest()

        random_type = random_plant[random() * len(random_plant) // 1]
        quick_print("random_ty = ", random_type)
        do_plant(random_type)

        while get_companion() != None:
            next_type, (nx, ny) = get_companion()
            quick_print("next_ty = ", random_type)
            quick_print("nx = ", nx)
            quick_print("ny = ", ny)
            move_to(nx, ny)
            if can_harvest():
                do_harvest()
            do_plant(next_type)


def run():
    reset_farm_state()
    play_companion()


run()
