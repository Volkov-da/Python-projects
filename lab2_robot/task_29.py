#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    pass
    i = 0
    while wall_is_on_the_right() == 0 and i < 3:
        if cell_is_filled() == 1:
            move_right()
            i += 1
        else:
            i = 0
            move_right()

    if i == 3:
        move_left()



if __name__ == '__main__':
    run_tasks()
