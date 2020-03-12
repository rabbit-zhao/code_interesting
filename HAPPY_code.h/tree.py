from turtle import *
import random
import time

n = 20.0
 
speed("fastest")
screensize(bg='seashell')
left(90)
forward(3*n)
color("orange", "yellow")
begin_fill()
left(126)

for i in range(5):
    forward(n/5)
    right(144)
    forward(n/5)
    left(72)
end_fill()
right(126)

color("dark green")
backward(n*4.8)
def tree(d, s):
    if d <= 0: return
    forward(s)
    tree(d-1, s*.8)
    right(120)
    tree(d-3, s*.5)
    right(120)
    tree(d-3, s*.5)
    right(120)
    backward(s)
tree(10, n)
backward(n/2)

for i in range(20):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    up()
    forward(b)
    left(90)
    forward(a)
    down()
    if random.randint(0, 1) == 0:
            color('tomato')
    else:
        color('wheat')
    circle(2)
    up()
    backward(a)
    right(90)
    backward(b)
time.sleep(1.5)

penup()
color("violet")
goto(-50,-100)
write(" 黄钰涵小朋友", font=("微软雅黑", 20, "normal"))
goto(-50,-140)
time.sleep(0.5)
color("green")
write("Merry Christmas",font=("微软雅黑", 20, "normal"))
time.sleep(0.5)
goto(-50,-180)
color("red")
write("Marry you !",font=("微软雅黑", 20, "normal"))
