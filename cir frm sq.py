import turtle
def draw_shape():
    window=turtle.Screen()
    window.bgcolor("red")

    jon=turtle.Turtle()
    jon.shape("turtle")
    jon.speed(99)
    jon.color("yellow")
    for i in range(1,37):
        draw_sq(jon)
        jon.right(10)

    window.exitonclick()



def draw_sq(bob):   
    i=1
    while(i<=4):
        bob.forward(100)
        bob.right(90)
        i+=1
       

draw_shape()
