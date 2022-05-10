from turtle import *
import random
speed(0)
colormode(255)
reset()
def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)

def offsetDownRight(offset):
    penup()
    forward(offset)
    right(90)
    forward(offset)
    left(90)
    pendown()


for i in range(18):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    fillcolor(r,g,b)
    begin_fill()
    square(100)
    end_fill()
    right(20)
    #offsetDownRight(10)

input("Finished, press enter to close")

