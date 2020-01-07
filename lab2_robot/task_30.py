#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_9_3():
    pass
    c = 0
    n = 0
    while wall_is_on_the_right() == 0:
        n += 1
        move_right()
    if wall_is_on_the_right() == 1:
        n -= 1
    print(n)

    c = int((n + 1) /2)
    print(c)

    def circule(n):
        i = 0
        move_down()
        while i < n:
            fill_cell()
            move_down()
            i += 1
        i = 0
        move_left()
        while i < n:
            fill_cell()
            move_left()
            i += 1
        i = 0
        move_up()
        while i < n:
            fill_cell()
            move_up()
            i += 1
        i = 0
        move_right()
        while i < n:
            fill_cell()
            move_right()
            i += 1
        move_left()
        move_down()


    while n >= 1:
        circule(n)
        n -= 2
    move_left(c)
    move_down(c)



if __name__ == '__main__':
    run_tasks()
