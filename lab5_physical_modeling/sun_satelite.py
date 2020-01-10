import graphics as gr

SIZE_X = 800
SIZE_Y = 800
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords_earth = gr.Point(400, 700)
coords_mars = gr.Point(400, 600)
velocity_earth = gr.Point(2, 0)
velocity_mars = gr.Point(2, 0)
acceleration_earth = gr.Point(0, 0)
acceleration_mars = gr.Point(0, 0)


# Обьект Earth создается здесь лишь ОДИН раз
earth = gr.Circle(coords_earth, 20)
earth.draw(window)
earth.setFill('blue')
earth.setOutline('blue')

# Обьект Mars создается здесь лишь ОДИН раз
mars = gr.Circle(coords_mars, 20)
mars.draw(window)
mars.setFill('red')
mars.setOutline('red')


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def add_tuple(point_1, point_2):
    x_new = (point_1.x + point_2.x, point_1.y + point_2.y)
    return x_new


def sub(point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x, point_1.y - point_2.y)
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
    coords_earth = update_coords(coords_earth, velocity_earth)
    coords_mars = update_coords(coords_mars, velocity_mars)

    acceleration_earth = update_acceleration(coords_earth, gr.Point(400, 400))
    acceleration_mars = update_acceleration(coords_earth, gr.Point(400, 400))

    velocity_earth = update_velocity(velocity_earth, acceleration_earth)
    velocity_mars = update_velocity(velocity_mars, acceleration_mars)

    velosity_earth_x, velosity_earth_y = add_tuple(velocity_earth, acceleration_earth)
    velosity_mars_x, velosity_mars_y = add_tuple(velocity_mars, acceleration_mars)

    earth.move(velosity_earth_x, velosity_earth_y)
    mars.move(velosity_mars_x, velosity_mars_y)



