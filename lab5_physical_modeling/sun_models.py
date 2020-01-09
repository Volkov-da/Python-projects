import graphics as gr

size_x = 800
size_y = 800

earth_velocity_x = 2
earth_velocity_y = 0

earth_acceleration_x = 0
earth_acceleration_y = 0

earth_position_x = 400
earth_position_y = 200

sun_position_x = 400
sun_position_y = 400

window = gr.GraphWin("System", size_x, size_y)

earth_coords = gr.Point(earth_position_x, earth_position_y)

sun = gr.Circle(gr.Point(sun_position_x, sun_position_y), 100)
sun.draw(window)
sun.setFill('yellow')

# Обьект Earth создается здесь лишь ОДИН раз
earth = gr.Circle(gr.Point(earth_position_x, earth_position_y), 20)
earth.draw(window)
earth.setFill('blue')
earth.setOutline('blue')


def add(x1, y1, x2, y2):
    new_x = x1 + x2
    new_y = y1 + y2

    return new_x, new_y

def sub(x1, y1, x2, y2):
    new_x = x1 - x2
    new_y = y1 - y2

    return new_x, new_y


def update_coordinates(earth_x, earth_y, earth_velosity_x, earth_velosity_y):
    return add(earth_x, earth_y, earth_velosity_x, earth_velosity_y)


def update_velocity(velocity_x, velocity_y, acceleration_x, acceleration_y):
    return add(velocity_x, velocity_y, acceleration_x, acceleration_y)


def update_acceleration(earth_position_x, earth_position_y, sun_position_x, sun_position_y):
    distance_x = earth_position_x - sun_position_x
    distance_y = earth_position_y - sun_position_y
    distance_tot = (distance_x ** 2 + distance_y ** 2) ** (3/2)
    G = 2000
    acceleration_x = -distance_x * G / distance_tot
    acceleration_y = -distance_y * G / distance_tot
    return acceleration_x, acceleration_y

while True:
    x_coord, y_coord = update_coordinates(earth_position_x, earth_position_y, earth_velocity_x, earth_velocity_y)
    x_acc, y_acc = update_acceleration(x_coord, y_coord, sun_position_x, sun_position_y)
    x_vel, y_vel = update_velocity(earth_velocity_x, earth_velocity_y, x_acc, y_acc)

    print('Coordinations:', x_coord, type(x_coord), y_coord, type(y_coord))
    print('Velosity:', x_vel, y_vel, type(y_vel))
    print('Acceleration:', x_acc, y_acc, type(y_acc))


