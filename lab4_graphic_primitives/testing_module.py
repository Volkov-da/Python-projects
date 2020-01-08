from graphics import *


def main():
    win = GraphWin("My Circle", 200, 200)
    c = Circle(Point(100, 100), 90)
    b = Circle(Point(100, 100), 80)
    d = Circle(Point(100, 100), 70)
    c.draw(win)
    b.draw(win)
    d.draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


main()
