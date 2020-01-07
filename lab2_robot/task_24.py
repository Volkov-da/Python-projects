#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    pass

    def cross():
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_right(2)
        fill_cell()
    move_right(2)
    move_down(1)
    cross()
    move_left(2)
    move_up()



if __name__ == '__main__':
    run_tasks()
