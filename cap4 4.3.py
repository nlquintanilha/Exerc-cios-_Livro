#teste
import turtle

def square(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
                         

bob = turtle.Turtle()

square(bob, 50)
bob.penup()
bob.goto(70, 0)
bob.pendown()
square(bob, 100)    
bob.penup()
bob.goto(200, 0)
bob.pendown()
square(bob, 150)    
bob.penup()
bob.goto(0, -200)
bob.pendown()

turtle.done()



