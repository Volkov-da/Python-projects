#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    pass
    move_right(2)
    move_down(2)
    fill_cell()
    move_right(2)
    move_down(1)

if __name__ == '__main__':
    run_tasks()
