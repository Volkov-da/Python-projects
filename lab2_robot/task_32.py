#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_18():
    pass
    i = 0
    j = 0
    counter = 0
    ax = []
    while wall_is_on_the_right() == 0:
        if wall_is_above() == 0:
            while wall_is_above() == 0:
                if cell_is_filled() == 1:
                    counter += 1
                    print(counter)
                move_up()
        if wall_is_above() == 1:
            if cell_is_filled() == 1:
                counter += 1
                print(counter)
            while wall_is_beneath() == 0:
                move_down()
            move_right()
            i += 1
        elif wall_is_above() == 1:
            if cell_is_filled() == 1:
                counter += 1
                print(counter)

            move_right()
            i += 1

    move_left(i)

    while j < i:
        if wall_is_above() == 0:
            while wall_is_above() == 0:
                move_up()
                fill_cell()
            while wall_is_beneath() == 0:
                move_down()
            move_right()
            j += 1
        elif wall_is_above() == 1:
            fill_cell()
            move_right()
            j += 1

    print(counter)
    mov(ax, counter)



if __name__ == '__main__':
    run_tasks()
