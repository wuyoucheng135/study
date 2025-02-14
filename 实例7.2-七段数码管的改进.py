import time
import turtle as t
def drawGap():
    t.penup()
    t.fd(5)
    t.pendown()
def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)
def drawDight(dight):
    drawLine(True) if dight in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,6,8] else drawLine(False)
    t.left(90)
    drawLine(True) if dight in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if dight in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if dight in [0,1,2,3,4,7,8,9] else drawLine(False)
    t.left(180)
    t.penup()
    t.fd(10)
    t.right(90)
    t.fd(50)
    t.dot(5)
    t.fd(-50)
    t.left(90)
    t.fd(10)
    t.pendown()
def drawDate(date):
    for i in date:
        if i=='-':
            t.write('年',font=('Arial',18,'normal'))
            t.pencolor('green')
            t.penup()
            t.fd(40)
        elif i=='=':
            t.write('月', font=('Arial', 18, 'normal'))
            t.pencolor('blue')
            t.penup()
            t.fd(40)
        elif i=='+':
            t.write('日', font=('Arial', 18, 'normal'))
            t.penup()
            t.fd(40)
        else:
            drawDight(eval(i))
def main ():
    t.setup(800,350,200,200)
    t.pencolor('red')
    t.penup()
    t.fd(-300)
    t.pensize(5)
    drawDate(time.strftime('%Y-%m=%d+',time.gmtime()))
    t.hideturtle()
    t.done()
main()