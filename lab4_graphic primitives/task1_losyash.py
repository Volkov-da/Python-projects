import graphics as gr
window = gr.GraphWin('Losyash', 350, 350)

eye1 = gr.Circle(gr.Point(110, 120), 20)
eye1.setFill('white')
eye1.setOutline('white')

eye2 = gr.Circle(gr.Point(205, 130), 20)
eye2.setFill('white')
eye2.setOutline('white')

eye1_center = gr.Circle(gr.Point(115, 125), 10)
eye1_center.setFill('black')

eye2_center = gr.Circle(gr.Point(200, 135), 10)
eye2_center.setFill('black')

nose = gr.Circle(gr.Point(140, 170), 30)
nose.setFill('yellow')
nose.setOutline('yellow')

body = gr.Circle(gr.Point(160, 150), 100)
body.setFill('brown')
body.setOutline('brown')

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

leg2 = gr.Line(gr.Point(120, 230), gr.Point(120, 290))
leg2.setWidth(40)
leg2.setOutline('brown')

leg1 = gr.Line(gr.Point(200, 230), gr.Point(200, 290))
leg1.setWidth(40)
leg1.setOutline('brown')

mouth = gr.Line(gr.Point(130, 215), gr.Point(180, 215))
mouth.setWidth(3)
mouth.setOutline('black')

tooth1 = gr.Line(gr.Point(145, 215), gr.Point(145, 225))
tooth1.setWidth(14)
tooth1.setOutline('white')

tooth2 = gr.Line(gr.Point(160, 215), gr.Point(160, 225))
tooth2.setWidth(14)
tooth2.setOutline('white')

# start drawing
ear1.draw(window)
ear1_center.draw(window)
ear2.draw(window)
ear2_center.draw(window)

body.draw(window)
nose.draw(window)

eye1.draw(window)
eye2.draw(window)

eye1_center.draw(window)
eye2_center.draw(window)

hand1.draw(window)
wrist1.draw(window)

hand2.draw(window)
wrist2.draw(window)

leg1.draw(window)
leg2.draw(window)

mouth.draw(window)
tooth1.draw(window)
tooth2.draw(window)

window.getMouse()

