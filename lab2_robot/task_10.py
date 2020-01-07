#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    pass
    while wall_is_on_the_right() == 0:
        if wall_is_beneath() == 1 or wall_is_above() == 1:
            fill_cell()
            move_right()
        else:
            move_right()
    if wall_is_above() == 1 or wall_is_beneath() == 1:
        fill_cell()

if __name__ == '__main__':
    run_tasks()
