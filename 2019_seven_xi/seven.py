import turtle as tl
import time

def hart_arc():
	for i in range(100):
		tl.speed(100)
		tl.right(2)
		tl.forward(4)

def move_pen_position(x, y):
	tl.hideturtle()
	tl.up()
	tl.goto(x, y)
	tl.down()
	tl.showturtle()

def write_in_heart(x, y):
	move_pen_position(x, y)
	tl.color('#CD5C5C', 'pink')
	tl.write(love + '\n', font=('Arial', 25, 'bold'), align='center')
	time.sleep(0.5)
	move_pen_position(x, y-35)
	tl.write(person+'\n', font=('Arial', 20, 'bold'), align='center')
	time.sleep(0.5)
	move_pen_position(x, y-30)
	tl.write("—— for Qixi", font=('Arial', 16, 'bold'), align='center')

def draw_heart(x, y):
	tl.color('red', 'pink')
	tl.pensize(3)
	tl.speed(1)
	move_pen_position(x, y)
	tl.left(140)
	tl.begin_fill()  # color begin
	tl.forward(224)

	hart_arc()  # left
	tl.left(120)
	hart_arc()  # right

	tl.forward(224)  # straight right

	tl.end_fill()  # end color
	

def draw_person(x, y, r, body, leg, c):   # head
	move_pen_position(x, y-r)
	tl.seth(0)
	if c==1:
		color = 'blue'
	elif c==2:
		color = 'dark orange'
	tl.color(color)
	tl.pensize(4)
	tl.speed(1.5)
	tl.circle(r)  # head
	# move_pen_position(x, -30)
	tl.seth(270)
	tl.forward(body) # body
	tl.right(30)
	tl.forward(leg)  # one leg
	tl.up()
	tl.right(180)
	tl.forward(leg)
	tl.down()
	tl.right(120)
	# move_pen_position(x, y)
	# tl.left(60)
	tl.forward(leg)

def draw_arm(y):
	tl.color("purple")

	tl.pensize(1.5)
	move_pen_position(-210, y)
	tl.seth(135)
	tl.forward(20)
	tl.right(135)
	tl.forward(40)
	tl.right(45)
	tl.forward(20)
	tl.right(90)
	tl.forward(20)
	tl.right(45)
	tl.forward(40)
	tl.right(135)
	tl.forward(20)

	tl.pensize(5)
	move_pen_position(220, y)
	tl.seth(135)
	tl.forward(23)
	move_pen_position(220, y)
	tl.seth(-135)
	tl.forward(23)
	time.sleep(1)

	tl.pensize(3)
	move_pen_position(-207, y)
	tl.seth(0)
	tl.forward(417)
	tl.hideturtle()

love = "The best time with you ! "
person = "Miss Zhang YF"

tl.setup(width=800, height=500)
draw_heart(0, -180)
r = 40
body = 50
leg = 100
draw_person(-60, -50, r, body, leg, 1)
draw_person(60, -50, r, body, leg, 2)
write_in_heart(0, 0)
draw_arm(-50-r-20)
