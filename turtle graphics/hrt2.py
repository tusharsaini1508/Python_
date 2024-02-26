from turtle import *
import colorsys

bgcolor('black')
tracer(500)

def draw():
    h = 0
    for i in range(100):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 0.5
        up()
        goto(0, 0)
        down()
        color('white')
        fillcolor(c)
        begin_fill()
        right(98)
        circle(i, 12)
        forward(i)
        left(29)
        for j in range(129):
            forward(i)
            circle(j, 299, steps=2)
        end_fill()

draw()
done()
