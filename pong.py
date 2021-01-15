import turtle
import numpy as np
import functools
import winsound

# generate a random color to be the base of our color scheme
color = np.random.rand(3,)
inverse = [abs(1-color[0]), abs(1-color[1]), abs(1-color[2])]


# create a screen - variable wn
wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor(color)
wn.setup(width=600, height=400)
wn.tracer(0)    # only manual updates to game screen - more efficient

# create game object - scoreboard
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color(inverse)
pen.penup()
pen.hideturtle()
pen.goto(0, 160)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

# create game objects - paddle a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color(inverse)
paddle_a.penup()
paddle_a.goto(-275, 0)

# create game objects - paddle b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color(inverse)
paddle_b.penup()
paddle_b.goto(270, 0)

# create game objects - ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color(inverse)
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = .1

# easy access of objects for functions
paddle = {'a': paddle_a, 'b': paddle_b}

# create functions


def up(key):
    y = paddle[key].ycor() + 20
    if y < 200:
        paddle[key].sety(y)


def down(key):
    y = paddle[key].ycor() - 20
    if y > -200:
        paddle[key].sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(functools.partial(up, 'a'), "w")
wn.onkeypress(functools.partial(down, 'a'), "s")
wn.onkeypress(functools.partial(up, 'b'), "Up")
wn.onkeypress(functools.partial(down, 'b'), "Down")

# create a game loop
while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() >= 190 or ball.ycor() <= -190:
        ball.dy = -1 * ball.dy
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if (-260 >= ball.xcor() >= -265 and abs(paddle_a.ycor() - ball.ycor()) <= 70) or \
            (258 >= ball.xcor() >= 253 and 70 >= abs(paddle_b.ycor() - ball.ycor())):
        ball.dx = -1 * ball.dx
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() <= -300 or ball.xcor() >= 300:
        ball.goto(0, 0)
        if ball.dx > 0:
            score_a += 1
        elif ball.dx < 0:
            score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        ball.dx = ball.dx * -1
        ball.dy = ball.dy * -1
