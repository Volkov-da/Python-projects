#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    pass
    while wall_is_on_the_right() == 0:
        if wall_is_above() == 0 and wall_is_beneath() == 1:
            move_up()
            fill_cell()
            move_down()
            move_right()
        elif wall_is_beneath() == 0 and wall_is_above() == 1:
            move_down()
            fill_cell()
            move_up()
            move_right()
        elif wall_is_above() == 0 and wall_is_beneath() == 0:
            move_up()
            fill_cell()
            move_down(2)
            fill_cell()
            move_up()
            move_right()
        else:
            move_right()

        if wall_is_above() == 1 and wall_is_beneath() == 0 and wall_is_on_the_right() == 1:
            move_down()
            fill_cell()
            move_up()
        if wall_is_above() == 0 and wall_is_beneath() == 1 and wall_is_on_the_right() == 1:
            move_up()
            fill_cell()
            move_down()
        if wall_is_beneath() == 0 and wall_is_above() == 0 and wall_is_on_the_right() == 1:
            move_up()
            fill_cell()
            move_down(2)
            fill_cell()
            move_up()

if __name__ == '__main__':
    run_tasks()
