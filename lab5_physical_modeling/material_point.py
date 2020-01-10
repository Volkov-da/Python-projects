import graphics as gr

SIZE_X = 400
SIZE_Y = 400
velocity = gr.Point(10, -2)
acceleration = gr.Point(0, 0.5)

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(200, 200)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)


def check_coords(coords, velocity):
    if coords.x < 15 or coords.x > SIZE_X - 15:
        velocity.x = -velocity.x

    if coords.y < 15 or coords.y > SIZE_Y - 15:
        velocity.y = -velocity.y


def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)


while True:
    clear_window()

    draw_ball(coords)
    coords = add(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.04)