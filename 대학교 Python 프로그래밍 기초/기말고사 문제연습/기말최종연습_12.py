# 좌클릭시 좌표 찍음, 우클릭시 화면 클리어

import turtle as t

def write_xy(x,y):
    t.goto(x, y)
    t.stamp()
    t.write("x좌표:%d, y좌표:%d"%(x,y))

def screen_clear(x,y):
    t.goto(x,y)
    t.clear()

t.setup(600, 600)
s = t.Screen()
t.penup()

s.onscreenclick(write_xy, 1)
s.onscreenclick(screen_clear, 3)
s.listen

t.mainloop()