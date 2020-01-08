import graphics as gr


window = gr.GraphWin('Losyash_functional', 500, 500)


def draw_body(length):
    body = gr.Circle(gr.Point(0.5 * length, 0.5 * length), 0.33 * length)
    body.setFill('brown')
    body.setOutline('brown')
    body.draw(window)


def draw_nose(length):
    """
    :param x: horizontal distance(x) between eyes. Value should be taken from "eyes" function
    :param y: vertical position of the nose. Correlated with body parameters, center of the body circle.
    :param radius: radius of the nose. About 15% of the body radius.
    """
    nose = gr.Circle(gr.Point(0.46 * length, 0.52 * length), 0.10 * length)
    nose.setFill('yellow')
    nose.setOutline('yellow')
    nose.draw(window)


def left_eye(length):
    """
    This function drawing left eye
    :param x: horizontal position of the eye
    :param y: vertical position of the eye
    :param radius: radius of the eye
    :return:
    """
    eye1 = gr.Circle(gr.Point(0.34 * length, 0.35 * length), 0.065 * length)
    eye1.setFill('white')
    eye1.setOutline('white')

    eye1_center = gr.Circle(gr.Point(0.35 * length, 0.36 * length), 0.035 * length)
    eye1_center.setFill('black')
    eye1.draw(window)
    eye1_center.draw(window)


def right_eye(length):
    """
    This function drawing right eye
    :param x: horizontal position of the eye
    :param y: vertical position of the eye
    :param radius: radius of the eye

    """
    eye2 = gr.Circle(gr.Point(0.6 * length, 0.33 * length), 0.065 * length)
    eye2.setFill('white')
    eye2.setOutline('white')
    eye2_center = gr.Circle(gr.Point(0.59 * length, 0.35 * length), 0.035 * length)
    eye2_center.setFill('black')
    eye2.draw(window)
    eye2_center.draw(window)


def ears(length):
    ear1 = gr.Circle(gr.Point(0.32 * length, 0.21 * length), 0.1 * length)
    ear1.setFill('brown')
    ear1.setOutline('brown')
    ear1_center = gr.Circle(gr.Point(0.32 * length, 0.21 * length), 0.06 * length)
    ear1_center.setFill('yellow')
    ear1_center.setOutline('yellow')

    ear2 = gr.Circle(gr.Point(0.67 * length, 0.20 * length), 0.1 * length)
    ear2.setFill('brown')
    ear2.setOutline('brown')
    ear2_center = gr.Circle(gr.Point(0.67 * length, 0.20 * length), 0.06 * length)
    ear2_center.setFill('yellow')
    ear2_center.setOutline('yellow')

    ear1.draw(window)
    ear2.draw(window)
    ear1_center.draw(window)
    ear2_center.draw(window)


def hands(length):
    hand1 = gr.Line(gr.Point(0.05 * length, 0.37 * length), gr.Point(0.2 * length, 0.43 * length))
    hand1.setOutline('brown')
    hand1.setWidth(0.09 * length)

    wrist1 = gr.Circle(gr.Point(0.05 * length, 0.37 * length), 0.043 * length)
    wrist1.setFill('brown')
    wrist1.setOutline('brown')

    hand2 = gr.Line(gr.Point(0.63 * length, 0.50 * length), gr.Point(0.95 * length, 0.40 * length))
    hand2.setWidth(0.09 * length)
    hand2.setOutline('brown')

    wrist2 = gr.Circle(gr.Point(0.95 * length, 0.40 * length), 0.043 * length)
    wrist2.setFill('brown')
    wrist2.setOutline('brown')

    hand1.draw(window)
    hand2.draw(window)
    wrist1.draw(window)
    wrist2.draw(window)


def legs(length):
    leg2 = gr.Line(gr.Point(0.36 * length, 0.66 * length), gr.Point(0.36 * length, 0.95 * length))
    leg2.setWidth(0.12 * length)
    leg2.setOutline('brown')

    leg1 = gr.Line(gr.Point(0.63 * length, 0.66 * length), gr.Point(0.63 * length, 0.95 * length))
    leg1.setWidth(0.12 * length)
    leg1.setOutline('brown')

    leg1.draw(window)
    leg2.draw(window)


def draw_mouth(length):
    mouth = gr.Line(gr.Point(0.40 * length, 0.65 * length), gr.Point(0.53 * length, 0.65 * length))
    mouth.setWidth(0.01 * length)
    mouth.setOutline('black')

    tooth1 = gr.Line(gr.Point(0.44 * length, 0.65 * length), gr.Point(0.44 * length, 0.68 * length))
    tooth1.setWidth(0.03 * length)
    tooth1.setOutline('white')

    tooth2 = gr.Line(gr.Point(0.48 * length, 0.65 * length), gr.Point(0.48 * length, 0.68 * length))
    tooth2.setWidth(0.03 * length)
    tooth2.setOutline('white')

    mouth.draw(window)
    tooth1.draw(window)
    tooth2.draw(window)


# start drawing
def full_picture(length):
    """
    This function will draw a funny animal.
    Parameter "length" will determine the sizes of this guy.
    This the only thing that should be determined here.
    """
    ears(length)
    draw_body(length)
    left_eye(length)
    right_eye(length)
    draw_nose(length)
    draw_mouth(length)
    hands(length)
    legs(length)


for i in range(0, 600, 100):
    full_picture(i)
window.getMouse()

