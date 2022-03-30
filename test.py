# import math

# def compute_circle_area(radius):
#     return radius**2 * math.pi

# def prompt_user_for_radius():
#     user_radius = float(input("please enter a radius: "))
#     return user_radius

# area = round(compute_circle_area(prompt_user_for_radius), 2)

# def display_area(area):
#     print(area)

# def func(x):
#   res = 0
#   for i in range(x):
#      res += i
#   return res

# print(func(4))

# def compute(x, y, z):
#     r= x+y+z
#     return r
# x = 7
# result = compute(3, 2, x)
# print(result)

# import random
# def draw_cloud(canvas, width, height, x_min, x_max, y_min, y_max):
#     for i in range(0,4):
#         x_start = random.randrange(x_min, x_max)
#         y_start = random.randrange(x_min, x_max)
#         count 

# def draw_clouds(number_of_clouds):
#     for i in range(number_of_clouds):
#         draw_cloud(..)

# import math
# def calculate_circle_area(radius):
#     return radius**2 * math.pi

# area = calculate_circle_area(5)
# print(area)

#prints every other letter in a word
# str = input("enter name: ")
# for i in range(0, len(str), 2):
#     print(str[i])

# r = {"hi helo", "heis", "hie"}
# print(len(r))
# import pytest
# pytest.__version__
# y = input("got milk").capitalize

# b = 1 if 2+2==5 else 5
# print(b)

# import random
# def quantitys():
#     quantity = random.randint(0,1)
#     return quantity
# print(quantitys())
# import numpy as np
# data = [5,5,4,5,6]
# # print(np.mean(data))
# print(np.percentile(data, 50))

# numbers = "1 2 3".split(" ")
# print(len(numbers))
# hi = [[1,2],[3,4],[5,6],[7,8],[9,10]]
# print(hi)

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# name = 'gallahad'
# for name in knights:
#     print('yes')

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits[1])

# video = {
#   "title": 'Awesome python tutorial',
#   "views": 54325,
#   "img": 'google.com/images.qer.png'
# }
# video2 = {
#   "title": 'Awesome C# tutorial',
#   "views": 21325,
#   "img": 'google.com/images.hiekdsr.png',
#   "comments": []
# }
# videos =[video, video2]

# # print(videos[0]['title'])
# for key, value in video2.items():
#   print(f"{key}: {value}" )


import turtle

screen = turtle.Screen()
screen.setup(800,800)
screen.title("Tic Tac Toe - PythonTurtle.Academy")
screen.setworldcoordinates(-5,-5,5,5)
screen.bgcolor('light gray')
screen.tracer(0,0)
turtle.hideturtle()

def draw_board():
    turtle.pencolor('green')
    turtle.pensize(10)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3,1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def draw_circle(x,y):
    turtle.up()
    turtle.goto(x,y-0.75)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.75, steps=100)

def draw_x(x,y):
    turtle.color('blue')
    turtle.up()
    turtle.goto(x-0.75,y-0.75)
    turtle.down()
    turtle.goto(x+0.75,y+0.75)
    turtle.up()
    turtle.goto(x-0.75,y+0.75)
    turtle.down()
    turtle.goto(x+0.75,y-0.75)
    
def draw_piece(i,j,p):
    if p==0: return
    x,y = 2*(j-1), -2*(i-1)
    if p==1:
        draw_x(x,y)
    else:
        draw_circle(x,y)
    
def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i,j,b[i][j])
    screen.update()

# return 1 if player 1 wins, 2 if player 2 wins, 3 if tie, 0 if game is not over
def gameover(b):
    if b[0][0]>0 and b[0][0] == b[0][1] and b[0][1] == b[0][2]: return b[0][0]
    if b[1][0]>0 and b[1][0] == b[1][1] and b[1][1] == b[1][2]: return b[1][0]
    if b[2][0]>0 and b[2][0] == b[2][1] and b[2][1] == b[2][2]: return b[2][0]
    if b[0][0]>0 and b[0][0] == b[1][0] and b[1][0] == b[2][0]: return b[0][0]
    if b[0][1]>0 and b[0][1] == b[1][1] and b[1][1] == b[2][1]: return b[0][1]
    if b[0][2]>0 and b[0][2] == b[1][2] and b[1][2] == b[2][2]: return b[0][2]
    if b[0][0]>0 and b[0][0] == b[1][1] and b[1][1] == b[2][2]: return b[0][0]
    if b[2][0]>0 and b[2][0] == b[1][1] and b[1][1] == b[0][2]: return b[2][0]
    p = 0
    for i in range(3):
        for j in range(3):
            p += (1 if b[i][j] > 0 else 0)
    if p==9: return 3
    else: return 0
    
def play(x,y):
    global turn
    i = 3-int(y+5)//2
    j = int(x+5)//2 - 1
    if i>2 or j>2 or i<0 or j<0 or b[i][j]!=0: return
    if turn == 'x': b[i][j], turn = 1, 'o'
    else: b[i][j], turn = 2, 'x'
    draw(b)
    r = gameover(b)
    if r==1:
        screen.textinput("Game over!","X won!")
    elif r==2:
        screen.textinput("Game over!","O won!")
    elif r==3:
        screen.textinput("Game over!", "Tie!")
    
b = [ [ 0,0,0 ], [ 0,0,0 ], [ 0,0,0 ] ]    
draw(b)
turn = 'x'
screen.onclick(play)
turtle.mainloop()