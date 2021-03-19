"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import up, goto, down, begin_fill, forward, left, \
    end_fill, setheading, right, onscreenclick, listen, onkey, \
    undo, color, done, setup, circle
from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle2(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    circle(0.5*((((start.x-end.x))**2+((start.y-end.y))**2)**0.5))
    end_fill()


def rectangle(start, end):
    "Draw rectangle from start to end."
    check = 0.0
    an = 90
    check = end.x - start.x
    up()
    goto(start.x, start.y)
    down()
    setheading(0)
    begin_fill()

    for count in range(2):
        # define length
        forward(check)
        if (check < 0):
            right(an)
        else:
            left(an)
        # define width
        forward(check*0.6)
        if (check < 0):
            right(an)
        else:
            left(an)
    end_fill()


def triangle(start, end):
    "Draw isosceles triangle from start to end."
    check = 0.0
    an = 120
    check = end.x - start.x
    up()
    goto(start.x, start.y)
    down()
    setheading(0)
    begin_fill()

    for count in range(3):
        # define size side
        forward(check)
        if (check < 0):
            right(an)
        else:
            left(an)
    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']
    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle2), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
