import turtle
import sys

# import array as arr
a = "X"
d = dict()


def board_setup():
    print("This code is desingned by Norbu Lama."
          "The first player is 'O' and second player is 'X'. ")
    print("Rules: \n"
          "1. Click on the box you wanna draw your mark \n"
          "2. The first player is 'O'\n"
          "3. Wait for turtle to draw the whole figure i.e. X or O")
    turtle.title("Norbu's Final Project Game: Tic Tac Toe")
    turtle.setup(300, 300)
    turtle.speed(8)
    turtle.pensize(5)
    turtle.bgcolor("black")
    turtle.pencolor('white')

    # horizontal lines
    y1 = 50
    x2 = -50
    for i in range(2):
        turtle.penup()
        turtle.goto(-150, y1)
        turtle.pendown()
        turtle.forward(300)
        y1 -= 100

    # Vertical lines
    for j in range(2):
        turtle.penup()
        turtle.goto(x2, 150)
        turtle.pendown()
        turtle.setheading(-90)
        turtle.forward(300)
        x2 += 100


def cross(box):
    turtle.pensize(4)
    turtle.pencolor('green')
    turtle.penup()

    if box == 1:
        turtle.goto(-100, 100)

    elif box == 2:
        turtle.goto(0, 100)

    elif box == 3:
        turtle.goto(100, 100)

    elif box == 4:
        turtle.goto(-100, 0)

    elif box == 5:
        turtle.goto(0, 0)

    elif box == 6:
        turtle.goto(100, 0)

    elif box == 7:
        turtle.goto(-100, -100)

    elif box == 8:
        turtle.goto(0, -100)

    elif box == 9:
        turtle.goto(100, -100)

    turtle.speed(8)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(30)
    turtle.backward(60)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.backward(60)
    turtle.penup()


def zero(box):
    turtle.pensize(4)
    turtle.pencolor('blue')
    turtle.penup()
    if box == 1:
        turtle.goto(-100, 100)

    elif box == 2:
        turtle.goto(0, 100)

    elif box == 3:
        turtle.goto(100, 100)

    elif box == 4:
        turtle.goto(-100, 0)

    elif box == 5:
        turtle.goto(0, 0)

    elif box == 6:
        turtle.goto(100, 0)

    elif box == 7:
        turtle.goto(-100, -100)

    elif box == 8:
        turtle.goto(0, -100)

    elif box == 9:
        turtle.goto(100, -100)

    turtle.setheading(0)
    turtle.right(90)
    turtle.forward(30)
    turtle.pendown()
    turtle.left(90)
    turtle.speed(12)
    turtle.circle(30)
    turtle.penup()


def is_winner():
    if len(d) >= 5:
        if 1 in d.keys() and 2 in d.keys() and 3 in d.keys():
            if d[1] == 'O' and d[2] == 'O' and d[3] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[1] == 'X' and d[2] == 'X' and d[3] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'X' WON THE GAME ")
                turtle.bye()
                sys.exit()
        if 4 in d.keys() and 5 in d.keys() and 6 in d.keys():
            if d[4] == 'O' and d[5] == 'O' and d[6] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[4] == 'X' and d[5] == 'X' and d[6] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'X' WON THE GAME ")
                turtle.bye()
                sys.exit()

        if 7 in d.keys() and 8 in d.keys() and 9 in d.keys():
            if d[7] == 'O' and d[8] == 'O' and d[9] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[7] == 'X' and d[8] == 'X' and d[9] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'X' WON THE GAME ")
                turtle.bye()
                sys.exit()

        if 1 in d.keys() and 4 in d.keys() and 7 in d.keys():
            if d[1] == 'O' and d[4] == 'O' and d[7] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[1] == 'X' and d[4] == 'X' and d[7] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'X' WON THE GAME ")
                turtle.bye()
                sys.exit()

        if 2 in d.keys() and 5 in d.keys() and 8 in d.keys():
            if d[2] == 'O' and d[5] == 'O' and d[8] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[2] == 'X' and d[5] == 'X' and d[8] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'X' WON THE GAME ")
                turtle.bye()
                sys.exit()
        if 1 in d.keys() and 4 in d.keys() and 7 in d.keys():
            if d[1] == 'O' and d[4] == 'O' and d[7] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[1] == 'X' and d[4] == 'X' and d[7] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
        if 3 in d.keys() and 6 in d.keys() and 9 in d.keys():
            if d[3] == 'O' and d[6] == 'O' and d[9] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[3] == 'X' and d[6] == 'X' and d[9] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
        if 1 in d.keys() and 5 in d.keys() and 9 in d.keys():

            if d[1] == 'O' and d[5] == 'O' and d[9] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[1] == 'X' and d[5] == 'X' and d[9] == 'X':
                print("CONGRATULATION !!! SECOND PLAYER 'X' WON THE GAME ")
                turtle.bye()
                sys.exit()
        if 3 in d.keys() and 5 in d.keys() and 7 in d.keys():

            if d[3] == 'O' and d[5] == 'O' and d[7] == 'O':
                print("CONGRATULATION !!! FIRST PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()
            elif d[3] == 'O' and d[5] == 'O' and d[7] == 'O':
                print("CONGRATULATION !!! SECOND PLAYER 'O' WON THE GAME ")
                turtle.bye()
                sys.exit()

    if len(d) == 9:
        print("ITS A DRAW GAME")
        turtle.bye()
        sys.exit()


def onclick(box):
    global a
    turtle.penup()
    if a == "X":
        zero(box)
        d[box] = "O"
        is_winner()
        print("Next turn 'X'")
        a = "O"
    else:
        cross(box)
        d[box] = "X"
        is_winner()
        print("Next Turn 'O'")
        a = "X"


def mouse_click(x, y):
    # print('you clicked',x,',',y)
    # determining box number.
    if -150 <= x <= -50 and 50 <= y <= 150:
        print('you clicked box 1')
        box = 1

    elif -50 <= x <= 50 and 50 <= y <= 150:
        print('you clicked box 2')
        box = 2

    elif 50 <= x <= 150 and 50 <= y <= 150:
        print('you clicked box 3')
        box = 3

    elif -150 <= x <= -50 and -50 <= y <= 50:
        print('you clicked box 4')
        box = 4

    elif -50 <= x <= 50 and -50 <= y <= 50:
        print('you clicked box 5')
        box = 5

    elif 50 <= x <= 150 and -50 <= y <= 50:
        print('you clicked box 6')
        box = 6

    elif -150 <= x <= -50 and -150 <= y <= -50:
        print('you clicked box 7')
        box = 7

    elif -50 <= x <= 50 and -150 <= y <= -50:
        print('you clicked box 8')
        box = 8

    elif 50 <= x <= 150 and -150 <= y <= -50:
        print('you clicked box 9')
        box = 9

    onclick(box)


board_setup()


def top():
    for i in range(1, 9):
        turtle.onscreenclick(mouse_click)


top()
turtle.done()
