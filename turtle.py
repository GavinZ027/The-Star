在Python中，你可以使用Turtle模块来画一只乌龟。Turtle是一个受Logo语言启发的图形库，它允许你创建图形。下面是一个简单的Python脚本，使用Turtle模块来画一只简单的乌龟形状：

```python
import turtle

# 创建画布和乌龟
screen = turtle.Screen()
t = turtle.Turtle()

# 设置乌龟的画笔颜色
t.color("green")

# 乌龟的头
t.penup()
t.goto(-20, 0)
t.pendown()
t.circle(40)

# 乌龟的身体
t.penup()
t.goto(-70, 0)
t.pendown()
t.circle(100)

# 乌龟的腿
t.penup()
t.goto(-70, -50)
t.pendown()
t.right(90)
t.forward(50)
t.backward(50)
t.right(90)

t.penup()
t.goto(-70, 50)
t.pendown()
t.right(90)
t.forward(50)
t.backward(50)
t.right(90)

t.penup()
t.goto(-120, 0)
t.pendown()
t.right(90)
t.forward(50)
t.backward(50)
t.right(90)

t.penup()
t.goto(-170, 0)
t.pendown()
t.right(90)
t.forward(50)
t.backward(50)
t.right(90)

# 乌龟的尾巴
t.penup()
t.goto(-220, 0)
t.pendown()
t.right(135)
t.forward(30)

# 乌龟的尾巴
t.penup()
t.goto(-220, -30)
t.pendown()
t.right(45)
t.forward(30)

# 隐藏乌龟的尾巴
t.hideturtle()

# 结束
screen.mainloop()
```
