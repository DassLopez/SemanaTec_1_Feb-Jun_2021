"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

<<<<<<< HEAD
from turtle import update, clear, ontimer, setup, \
    hideturtle, tracer, listen, onkey, done
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
banco = ['green', 'purple', 'black', 'orange', 'blue']
snake_colour = randrange(0, 4)
food_colour = randrange(0, 4)

while (snake_colour == food_colour):
    food_colour = randrange(0, 4)

snake_colour_str = banco[snake_colour]
food_colour_str = banco[food_colour]
=======
from turtle import clear, update, ontimer, setup, hideturtle, tracer, listen, \
     onkey, done
from random import randrange
from freegames import square, vector
from random import randint
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
>>>>>>> absalon/main


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
<<<<<<< HEAD
=======

>>>>>>> absalon/main
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
<<<<<<< HEAD
    snake.append(head)
=======

    snake.append(head)

>>>>>>> absalon/main
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
<<<<<<< HEAD
    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_colour_str)

    square(food.x, food.y, 9, food_colour_str)
=======

        if randint(0, 1) == 0:
            valor = randrange(-1, 2)
            print(valor)
            food.x = food.x+(valor * 10)
            if food.x == 140:
                food.x = food.x-20
            if food.x == -140:
                food.x = food.x + 20
        else:
            valor = randrange(-1, 2)
            food.y = food.y + (valor * 10)
            if food.y == 140:
                food.y = food.y - 20
            if food.y == -140:
                food.y = food.y + 20
    clear()
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
>>>>>>> absalon/main
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
