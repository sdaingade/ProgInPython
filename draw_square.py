import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)


    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100) #radius
    
    swapnil = turtle.Turtle()
    swapnil.forward(100)
    swapnil.right(120)
    swapnil.forward(100)
    swapnil.right(120)
    swapnil.forward(100)
    swapnil.right(120)
    
    window.exitonclick()

draw_square()