#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    pass
    i = 0
    while i < 5:
        move_right()
        if cell_is_filled():
            i += 1


if __name__ == '__main__':
    run_tasks()
