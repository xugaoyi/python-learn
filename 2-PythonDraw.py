# 画一条蟒蛇
import turtle # 导入绘图模块：海龟
turtle.setup(650, 350, 500, 200) # 设置窗口大小和启动位置（winth，height，statrX，startY） 此函数非必须，启动位置参数可选
turtle.penup() # 抬笔
turtle.fd(-250) # fd向前行进
turtle.pendown() # 落笔
turtle.pensize(25) # 笔的大小
turtle.pencolor("red") # 笔的颜色
turtle.seth(-40) # 改变角度为-40度
for i in range(4):
  turtle.circle(40, 80)
  turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40) # fd向前行进40像素
turtle.circle(16, 180)
turtle.fd(40 * 2/3)  # fd向前行进
turtle.done() # 完成
