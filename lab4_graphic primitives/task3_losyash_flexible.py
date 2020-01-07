import graphics as gr


window = gr.GraphWin('Losyash_functional', 350, 350)


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


def left_eye(x, y, radius):
    """
    This function drawing left eye
    :param x: horizontal position of the eye
    :param y: vertical position of the eye
    :param radius: radius of the eye
    :return:
    """
    eye1 = gr.Circle(gr.Point(x, y), radius)
    eye1.setFill('white')
    eye1.setOutline('white')

    eye1_center = gr.Circle(gr.Point(x + 5, y + 5), radius / 2)
    eye1_center.setFill('black')
    eye1.draw(window)
    eye1_center.draw(window)


def right_eye(x, y, radius):
    """
    This function drawing right eye
    :param x: horizontal position of the eye
    :param y: vertical position of the eye
    :param radius: radius of the eye

    """
    eye2 = gr.Circle(gr.Point(x, y), radius)
    eye2.setFill('white')
    eye2.setOutline('white')
    eye2_center = gr.Circle(gr.Point(x - 5, y + 5), radius / 2)
    eye2_center.setFill('black')
    eye2.draw(window)
    eye2_center.draw(window)


def eyes(x, y, radius):
    """
    This function will draw two eyes
    :param x: horizontal distance(x) between eyes
    :param y: vertical position of both eyes
    :param radius: radius of eye
    :return:

    """
    x1 = x - 45
    x2 = x + 45
    left_eye(x1, y, radius)
    right_eye(x2, y, radius)



def ears():
    ear1 = gr.Circle(gr.Point(110, 60), 30)
    ear1.setFill('brown')
    ear1.setOutline('brown')
    ear1_center = gr.Circle(gr.Point(110, 60), 20)
    ear1_center.setFill('yellow')
    ear1_center.setOutline('yellow')
    ear2 = gr.Circle(gr.Point(235, 75), 30)
    ear2.setFill('brown')
    ear2.setOutline('brown')
    ear2_center = gr.Circle(gr.Point(235, 75), 20)
    ear2_center.setFill('yellow')
    ear2_center.setOutline('yellow')

    ear1.draw(window)
    ear2.draw(window)
    ear1_center.draw(window)
    ear2_center.draw(window)


def hands():
    hand1 = gr.Line(gr.Point(20, 120), gr.Point(70, 150))
    hand1.setOutline('brown')
    hand1.setWidth(30)

    wrist1 = gr.Circle(gr.Point(20, 120), 15)
    wrist1.setFill('brown')
    wrist1.setOutline('brown')

    hand2 = gr.Line(gr.Point(220, 170), gr.Point(300, 140))
    hand2.setWidth(30)
    hand2.setOutline('brown')

    wrist2 = gr.Circle(gr.Point(300, 139), 15)
    wrist2.setFill('brown')
    wrist2.setOutline('brown')

    hand1.draw(window)
    hand2.draw(window)
    wrist1.draw(window)
    wrist2.draw(window)


def legs():
    leg2 = gr.Line(gr.Point(120, 230), gr.Point(120, 290))
    leg2.setWidth(40)
    leg2.setOutline('brown')

    leg1 = gr.Line(gr.Point(200, 230), gr.Point(200, 290))
    leg1.setWidth(40)
    leg1.setOutline('brown')

    leg1.draw(window)
    leg2.draw(window)


def mouth():
    mouth = gr.Line(gr.Point(130, 215), gr.Point(180, 215))
    mouth.setWidth(3)
    mouth.setOutline('black')

    tooth1 = gr.Line(gr.Point(145, 215), gr.Point(145, 225))
    tooth1.setWidth(14)
    tooth1.setOutline('white')

    tooth2 = gr.Line(gr.Point(160, 215), gr.Point(160, 225))
    tooth2.setWidth(14)
    tooth2.setOutline('white')

    mouth.draw(window)
    tooth1.draw(window)
    tooth2.draw(window)


# start drawing
def draw_face():
    eyes()
    mouth()


def draw_torso():
    ears()
    legs()
    hands()


def draw_losyash():
    draw_torso()
    draw_face()


def full_picture(length):
    draw_body(length)
    draw_nose(length)
    window.getMouse()


full_picture(350)

