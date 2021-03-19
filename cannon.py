"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""

from random import randrange
<<<<<<< HEAD
from turtle import clear, goto, dot, update, ontimer, setup, \
    hideturtle, up, tracer, onscreenclick, done
=======
from turtle import clear, goto, dot, update, ontimer, setup, hideturtle, \
     tracer, onscreenclick, done, up
>>>>>>> absalon/main
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
<<<<<<< HEAD
        speed.x = (x + 400) / 25
        speed.y = (y + 400) / 25
=======
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10
>>>>>>> absalon/main


def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200


<<<<<<< HEAD
def draw(c_tar, c_ball):
=======
def draw():
>>>>>>> absalon/main
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
<<<<<<< HEAD
        dot(20, c_tar)

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, c_ball)
=======
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')
>>>>>>> absalon/main

    update()


def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
<<<<<<< HEAD
        target.x -= 3  # 0.5

    if inside(ball):
        speed.y -= 0.35
=======
        target.x -= 5  # 0.5

    if inside(ball):
        speed.y -= .35
>>>>>>> absalon/main
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
<<<<<<< HEAD
        if (abs(target - ball) > 13):
            targets.append(target)

    dupe2 = targets.copy()
    targets.clear()

    for target in dupe2:
        if not inside(target):
            y = randrange(-150, 150)
            target.x = 200
            target.y = y
        targets.append(target)
    draw('blue', 'red')
=======
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

>>>>>>> absalon/main
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
