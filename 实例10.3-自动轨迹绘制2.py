import turtle

# 数据读取
dates = []
with open('date.txt') as f:
    for line in f:
        # 将每行数据转换为整数列表
        parts = list(map(int, line.strip().split(',')))
        if len(parts) == 6:  # 确保数据格式正确
            dates.append(parts)

# 初始化Turtle
t = turtle.Turtle()
t.speed(0)  # 设置最快绘制速度
t.pensize(2)  # 设置画笔粗细
turtle.colormode(255)  # 设置颜色模式为RGB 0-255

# 自动绘制
for data in dates:
    # 解析数据
    distance, turn_dir, angle, r, g, b = data

    # 设置画笔颜色（将0/1转换为0/255）
    t.pencolor(r * 255, g * 255, b * 255)

    # 转向控制
    if turn_dir == 1:
        t.left(angle)
    else:
        t.right(angle)

    # 前进绘制
    t.forward(distance)

turtle.done()  # 保持窗口打开