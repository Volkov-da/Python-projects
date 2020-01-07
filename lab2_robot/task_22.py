#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    pass
    fill_cell()
    while wall_is_beneath() == 0:
        while wall_is_on_the_right() == 0:
            fill_cell()
            move_right()
            fill_cell()
        move_down()
        while wall_is_on_the_left() == 0:
            fill_cell()
            move_left()
            fill_cell()
if __name__ == '__main__':
    run_tasks()
