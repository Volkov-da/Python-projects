#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    pass
    j = 0
    while j < 13:
        move_down()
        j += 1
        i = 0
        while i < j:
            move_right()
            fill_cell()
            i += 1
        move_left(j)
    move_down()
    move_right()




if __name__ == '__main__':
    run_tasks()
