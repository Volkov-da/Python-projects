import graphics as gr
window = gr.GraphWin('testing_window', 1000, 1000)


# Создание круга с радиусом 10 и координатами центра (50, 50)
my_circle = gr.Circle(gr.Point(500, 500), 100)

# Создание отрезка с концами в точках (2, 4) и (4, 8)
my_line = gr.Line(gr.Point(200, 400), gr.Point(40, 80))

# Создание прямоугольника у которого диагональ — отрезок с концами в точках (2, 4) и (4, 8)
my_rectangle = gr.Rectangle(gr.Point(200, 400), gr.Point(40, 80))

# Отрисовка примитивов в окне window
my_circle.draw(window)
my_line.draw(window)
my_rectangle.draw(window)

window.getMouse()
window.close()