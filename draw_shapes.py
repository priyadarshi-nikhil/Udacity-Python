import turtle
def draw_shapes():
    window=turtle.Screen()
    window.bgcolor("red")

    draw_sq()
    draw_cir()
    draw_tri()
    window.exitonclick()

def draw_sq():
    shawn = turtle.Turtle()
    shawn.shape("arrow")
    shawn.speed(2)
    shawn.color("yellow")

    i=1
    while (i<=4):
        shawn.forward(100)
        shawn.right(90)
        i+=1

def draw_cir():
    cindy = turtle.Turtle()
    cindy.shape("circle")
    cindy.speed(2)
    cindy.color("white")

    cindy.circle(100)

def draw_tri():
    troy = turtle.Turtle()
    troy.shape("classic")
    troy.speed(2)
    troy.color("grey")

    i=1
    while (i<=3):
        troy.forward(100)
        troy.right(120)
        i+=1

draw_shapes()

    
    

    
