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

video = {
  "title": 'Awesome python tutorial',
  "views": 54325,
  "img": 'google.com/images.qer.png'
}
video2 = {
  "title": 'Awesome C# tutorial',
  "views": 21325,
  "img": 'google.com/images.hiekdsr.png',
  "comments": []
}
videos =[video, video2]

# print(videos[0]['title'])
for key, value in video2.items():
  print(f"{key}: {value}" )


