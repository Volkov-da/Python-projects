#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_8_30():
    pass
    i = 0
    c = 0
    while c < 15:
        if wall_is_beneath() == 0:
            move_down()
        elif wall_is_on_the_left() == 0 and wall_is_beneath() == 1:
            while wall_is_on_the_left() == 0 and wall_is_beneath() == 1:
                move_left()
            c += 1 #достиг правого края
            print('Perv:', c)
        else:
            while wall_is_on_the_right() == 0 and wall_is_beneath() == 1:
                move_right()
            c += 1 # достиг левого края
            print('Vtor:', c)
        print(c)
    else:
        while wall_is_on_the_left() == 0:
            move_left()





if __name__ == '__main__':
    run_tasks()
