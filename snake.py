"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

# lista de colores que se pueden usar
colors = ["blue", "green", "orange", "yellow", "purple"]

# se selecciona un color aleatorio de la lista
snake_color = colors[randrange(len(colors))]
food_color = colors[randrange(len(colors))]

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def food_inside(food):
    #Return true if food is inside boundaries
    return -200 < food.x < 190 and -200 < food.y < 190

def rand_move(food):
    direction = randrange(0, 4)
    #random move direction
    originalX, originalY = food.x, food.y
    if direction == 0:
        food.x += 10
    elif direction == 1:
        food.y += 10
    elif direction == 2:
        food.x -= 10
    elif direction == 3:
        food.y -= 10
    """ if the new position is outside boundaries, revert movement and 
    call the function again to create a new move"""
    if not food_inside(food):
        food.x = originalX
        food.y = originalY
        rand_move(food)

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        #Move food if not eaten
        rand_move(food)
        snake.pop(0)

    clear()

    for body in snake:
        # se pone el color que se escogió aleatoriamente
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
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
