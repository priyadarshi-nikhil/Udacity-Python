import turtle

def draw_init():
    window=turtle.Screen()
    window.bgcolor("red")

    draw_n()
   # draw_space()
    draw_p()

    window.exitonclick()

def draw_space():
    mac = turtle.Turtle()
    mac.penup()
    mac.goto(50,0)
    mac.pendown()    
    
def draw_n():


    mac = turtle.Turtle()
    mac.speed(2)
    mac.shape("arrow")
    mac.color("grey")
    mac.penup()
    mac.goto(-50,0)
    mac.pendown()

    mac.left(90)
    mac.forward(100)
    mac.right(135)
    mac.forward(100)
    mac.left(135)
    mac.forward(100)
    mac.ht()
 

def draw_p():
 

    mac = turtle.Turtle()
    mac.speed(2)
    mac.shape("arrow")
    mac.color("grey")
    mac.penup()
    mac.goto(50,0)
    mac.pendown()

    mac.left(90)
    mac.forward(100)
    for i in range(0,3):
        mac.right(90)
        mac.forward(50)
    mac.ht() 

draw_init()

