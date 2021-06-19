import turtle as t
import math
def circleDraw(r):
    turtle_msg = '반지름'+str(r)+'인 원의 넓이 ='+str(r*r*math.pi)
    t.write(turtle_msg)
    t.circle(r)

r = int(input('반지름 :'))
circleDraw(r)