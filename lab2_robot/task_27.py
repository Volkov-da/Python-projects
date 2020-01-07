#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    length = 0
    move_right()
    while wall_is_on_the_right() == 0:
        fill_cell()
        length += 1
        for i in range(length):
            move_right()
            if wall_is_on_the_right() == 1:
                break


if __name__ == '__main__':
    run_tasks()
