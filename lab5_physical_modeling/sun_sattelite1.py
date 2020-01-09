from math import pi, cos, sin

import graphics as gr

SIZE_X = 800
SIZE_Y = 800
velocity = gr.Point(2, 0)
window = gr.GraphWin("System", SIZE_X, SIZE_Y)
coordinate_x = 400
coordinate_y = 200
coords = gr.Point(coordinate_x, coordinate_y)

# Обьект Earth создается здесь лишь ОДИН раз
earth = gr.Circle(gr.Point(coordinate_x, coordinate_y), 20)
earth.draw(window)
earth.setFill('blue')
earth.setOutline('blue')

mars = gr.Circle(gr.Point(400, 600), 15)
mars.draw(window)
mars.setFill('red')
mars.setOutline('red')

sun = gr.Circle(gr.Point(400, 400), 100)
sun.draw(window)
sun.setFill('yellow')
# sun.setOutline('yellow')
A = 0


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def update_coords(coords, velocity):
    return add(coords, velocity)


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000
    x_new = - diff.x * G/distance
    y_new = - diff.y * G / distance
    return x_new, y_new


while True:
    coords = update_coords(coords, velocity)
    A += 1
    Fi = A * pi / 180

    x = (4 * cos(Fi))
    y = (5 * sin(Fi))

    x1 = (- 5 * cos(Fi))
    y1 = (- 4 * sin(Fi))

    earth.move(x, y)
    coordinate_x += x
    coordinate_y += y
    print(coordinate_x, coordinate_y)
    mars.move(x1, y1)

    gr.time.sleep(0.02)

