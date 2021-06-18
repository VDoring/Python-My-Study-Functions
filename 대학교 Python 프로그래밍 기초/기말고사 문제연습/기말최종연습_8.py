# 유저가 입력한 반지름값으로 원 그리기
import turtle as t
import math

def circle_draw(radius):
    t.circle(radius)

user_radius = int(input('반지름 : '))
print('반지름 %d인 원의 넓이 ='%user_radius, user_radius*user_radius*math.pi)
circle_draw(user_radius)