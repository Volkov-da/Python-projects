#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    pass
    i = 0
    def cross():
        fill_cell()
        move_up()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_right(2)
        fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up()

    move_right(1)
    move_down(2)
    while i < 4:
        cross()
        move_right(4)
        i += 1
    cross()
    move_up()
    move_left()





if __name__ == '__main__':
    run_tasks()
