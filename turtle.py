import turtle

# 创建一个turtle画布
t = turtle.Turtle()

# 设置乌龟的速度和颜色
t.speed(1)  # 设置速度为1，最慢的速度
t.color("green")  # 设置乌龟的颜色为绿色

# 绘制乌龟的头
t.circle(50)

# 绘制乌龟的身体
t.penup()
t.goto(0, -50)  # 将乌龟移动到合适的位置
t.pendown()
t.circle(100)

# 绘制乌龟的四条腿
# 第一条腿
t.penup()
t.goto(50, 50)  # 移动到右上角
t.pendown()
t.forward(50)
# 第二条腿
t.penup()
t.goto(50, -50)  # 移动到右下角
t.pendown()
t.forward(50)
# 第三条腿
t.penup()
t.goto(-50, 50)  # 移动到左上角
t.pendown()
t.forward(50)
# 第四条腿
t.penup()
t.goto(-50, -50)  # 移动到左下角
t.pendown()
t.forward(50)

# 绘制乌龟的尾巴
t.penup()
t.goto(-75, 0)  # 移动到左侧
t.pendown()
t.left(60)  # 以左60度的角度
t.forward(50)
t.right(120)  # 右转120度
t.forward(50)

# 隐藏乌龟
t.hideturtle()

# 显示绘图窗口
turtle.done()
