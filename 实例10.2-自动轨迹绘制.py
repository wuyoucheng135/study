#autoTraceDraw.py
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,500,0,0)
t.pencolor('red')
t.pensize(5)


#数据读取
dates=[]
f=open('date.txt')
for line in f :
    line.replace('','\n')
    d=line.split(',')
    print(d,type(d))
    dates.append(list(map(eval,d)))
f.close()


#自动轨迹绘制
for i in range(len(dates)):
    t.fd(dates[i][0])
    if dates[i][1]:
        t.left(dates[i][2])
    else:
        t.right(dates[i][2])
    t.pencolor(dates[i][3],dates[i][4],dates[i][5])
t.done()