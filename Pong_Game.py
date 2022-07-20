# imported tutle module 
from tkinter import CENTER, font
import turtle

wind = turtle.Screen() #intialize screen 
wind.title("Ping Pong By Mohammad") # set the title of the window 
wind.bgcolor("black") # set the background color of the window
wind.setup(width=800, height=600) # set the wdth and height of the window 
wind.tracer(0)# stops the window from updating automatically

# kepp1 
kepp1 = turtle.Turtle() # intializes turtle object (shape)
kepp1.speed(0) # set the speed of the animation 
kepp1.shape("square") # set the shape of the object 
kepp1.color("blue") # set the color of the shape 
kepp1.shapesize(stretch_wid=5, stretch_len=1) # stretches the shape to meet the size 
kepp1.penup() # stops the object from drawing lines 
kepp1.goto(-350, 0) # set the position of the object 

# kepp2
kepp2 = turtle.Turtle()
kepp2.speed(0)
kepp2.shape("square")
kepp2.color("red")
kepp2.shapesize(stretch_wid=5, stretch_len=1)
kepp2.penup()
kepp2.goto(350, 0)

# ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# score 
score1 = 0
score2 = 0
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Mohammad: 0 Master: 0", align="center", font=("Courier", 24, "normal"))
# functions 
def kepp1_up(): 
    y = kepp1.ycor() # set the y coordinate of the keeper
    y += 20  # set the y to increase be 20
    kepp1.sety(y) # set the y of the kepper to the new coordinate

def kepp1_down(): 
    y = kepp1.ycor()
    y -= 20  # set the y to decrease be 20
    kepp1.sety(y)

def kepp2_up(): 
    y = kepp2.ycor()
    y += 20 
    kepp2.sety(y)

def kepp2_down(): 
    y = kepp2.ycor()
    y -= 20 
    kepp2.sety(y)


# kewbord bindings 
wind.listen() # tell the window to expect key input 
wind.onkeypress(kepp1_up, "w") # when pressing w the function kepp1_up is invoked 
wind.onkeypress(kepp1_down, "s")
wind.onkeypress(kepp2_up, "Up")
wind.onkeypress(kepp2_down, "Down")

# main game loop 
while True: 
    wind.update() # updates the screen everytime the loop run 

    # move the ball 
    ball.setx(ball.xcor() + ball.dx) #ball starts at 0 and evertime loop run ------>+0.05xaxis 
    ball.sety(ball.ycor() + ball.dy) # ball starts at 0 and evertime loop run ------>+0.05 yaxis 

    # border check , top border +300, bottom border -300px, ball is 20px 
    if ball.ycor() > 290: # if ball is at top border 
        ball. sety(290) # set y cordinate +290
        ball.dy *= -1 # reverse direction, making +0.05 ----> -0.05

    if ball.ycor() <-290: # if ball at right border 
        ball. sety(-290)
        ball.dy *= -1 

    if ball.xcor() >390: # if ball is right border 
        ball.goto(0, 0) # return ball to center 
        ball.dx *= -1 # reverse the x direction 
        score1 += 1 
        score.clear()
        score.write("Mohammad: {} Master {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() <-390: # if ball is at left border 
       ball.goto(0, 0)
       ball.dx *= -1
       score2 += 1 
       score.clear()
       score.write("Mohammad: {} Master: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
       

    # kepper and ball 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < kepp2.ycor() +  40 and  ball.ycor() > kepp2.ycor() - 40 ): 
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < kepp1.ycor() +  40 and  ball.ycor() > kepp1.ycor() - 40 ): 
        ball.setx(-340)
        ball.dx *= -1

    


