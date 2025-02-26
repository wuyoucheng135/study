import turtle
def koch(n,sise):
    if n==0:
        turtle.fd(sise)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            koch(n-1,sise/3)
def main():
    level=4
    Sise=400
    turtle.color('green')
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    koch(level,Sise)
    turtle.right(120)
    koch(level,Sise)
    turtle.right(120)
    koch(level,Sise)
    turtle.hideturtle()
    turtle.done()
main()
