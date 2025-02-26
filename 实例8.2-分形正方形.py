import turtle
def frac_square(n,size):
    if n==0 :
        turtle.fd(size)
    else:
        for angle in [0,90,-90,-90,90]:
            turtle.left(angle)
            frac_square(n-1,size/3)
def perfect_square(n,size):
    for i in range(4):
        frac_square(n,size)
        turtle.right(90)

def main():
    level,Size=2,100
    turtle.setup(600,600)
    turtle.penup()
    turtle.goto(-100,0)
    turtle.pendown()
    turtle.color('red')
    perfect_square(level,Size)
    turtle.done()
    turtle.hideturtle()
main()