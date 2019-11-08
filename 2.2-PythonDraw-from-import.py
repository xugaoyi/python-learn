# 画一条蟒蛇
from turtle import * # 导入绘图模块：海龟，并将模块中的所有函数导入
setup(650, 350, 500, 200) # 设置窗口大小和启动位置（winth，height，statrX，startY） 此函数非必须，启动位置参数可选
penup() # 抬笔
fd(-250) # fd向前行进
pendown() # 落笔
pensize(25) # 笔的大小
pencolor("red") # 笔的颜色
seth(-40) # 改变角度为-40度
for i in range(4):
  circle(40, 80)
  circle(-40, 80)
circle(40, 80/2)
fd(40) # fd向前行进40像素
circle(16, 180)
fd(40 * 2/3)  # fd向前行进
done() # 完成
