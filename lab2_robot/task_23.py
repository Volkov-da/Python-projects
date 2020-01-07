#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    pass
    j = 0
    i = 0
    while wall_is_on_the_right() == 0:
        move_right()
        j += 1
    while i < j:
        if wall_is_above() == 0:
            while wall_is_above() == 0:
                move_up()
                fill_cell()
            while wall_is_beneath() == 0:
                move_down()
            move_left()
            i += 1
        elif wall_is_above() == 1:
            move_left()
            i += 1



if __name__ == '__main__':
    run_tasks()
