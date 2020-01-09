import graphics as gr

SIZE_X = 800
SIZE_Y = 800

coordinate_x = 400
coordinate_y = 700

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(400, 700)
velocity = gr.Point(2, 0)
acceleration = gr.Point(0, 0)


# Обьект Earth создается здесь лишь ОДИН раз
earth = gr.Circle(gr.Point(coordinate_x, coordinate_y), 20)
earth.draw(window)
earth.setFill('blue')
earth.setOutline('blue')


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)


    return new_point


def add_tuple(point_1, point_2):
    x_new = (point_1.x + point_2.x, point_1.y + point_2.y)

    return x_new


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)

    return new_point

def draw_sun():
    sun = gr.Circle(gr.Point(400, 400), 50)
    sun.setFill('yellow')
    sun.draw(window)

def update_coords(coords, velocity):
    return add(coords, velocity)


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000
    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)

draw_sun()

while True:
    coords = update_coords(coords, velocity)
    acceleration = update_acceleration(coords, gr.Point(400, 400))
    velocity = update_velocity(velocity, acceleration)
    velosity_x, velosity_y = add_tuple(velocity, acceleration)
    earth.move(velosity_x, velosity_y)


