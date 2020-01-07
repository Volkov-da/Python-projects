#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    pass
    while cell_is_filled() == 0:
        move_up()
    move_left()
    if cell_is_filled() == 0:
        move_right(2)


if __name__ == '__main__':
    run_tasks()
