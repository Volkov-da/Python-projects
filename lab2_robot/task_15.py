#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    pass
    if wall_is_above() == 1 and wall_is_on_the_right() == 1:
        move_left(9)
        move_down(9)
    elif wall_is_above() == 1 and wall_is_on_the_left() == 1:
        move_right(9)
        move_down(9)
    elif wall_is_beneath() == 1 and wall_is_on_the_left() == 1:
        move_right(9)
        move_up(9)
    else:
        move_left(9)
        move_up(9)

if __name__ == '__main__':
    run_tasks()
