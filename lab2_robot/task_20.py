#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    pass
    j = 0
    while j < 6:
        i = 0
        move_right()
        while i < 27:
            fill_cell()
            move_right()
            i += 1
        move_down()
        move_left()
        i = 0
        while i < 27:
            fill_cell()
            move_left()
            i += 1
        move_down()
        j += 1
    move_right()

if __name__ == '__main__':
    run_tasks()
