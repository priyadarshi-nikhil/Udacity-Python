import turtle
def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    rick=turtle.Turtle()
    rick.shape("turtle")
    rick.color("yellow")
    rick.speed(99)

    for i in range (1,37 ):
        draw_quad(rick)
        rick.right(10)
    rick.right(90)
    rick.forward(300)
    window.exitonclick()

def draw_quad(bob):
    bob.left(15)
    bob.forward(150)
    bob.right(75)
    bob.forward(150)
    bob.right(105)
    bob.forward(150)
    bob.right(75)
    bob.forward(150)

draw_art()
