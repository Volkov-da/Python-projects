#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    pass
    i = 0
    j = 0
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

    move_right()
    move_down()
    while j < 4:
        i = 0
        while i < 9:
            cross()
            i += 1
            move_right(4)
        else:
            cross()
        move_left(36)
        move_down(4)
        j += 1
    else:
        i = 0
        while i < 9:
            cross()
            i += 1
            move_right(4)
        else:
            cross()
        move_left(37)
        move_up()




if __name__ == '__main__':
    run_tasks()
