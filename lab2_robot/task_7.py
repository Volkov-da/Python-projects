#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    pass
    while wall_is_beneath() == 0:
        move_down()
    while wall_is_beneath() == 1:
        move_right()
    move_down()
    move_left()
    while wall_is_above() == 1 and wall_is_on_the_left() == 0:
        move_left()

if __name__ == '__main__':
    run_tasks()
