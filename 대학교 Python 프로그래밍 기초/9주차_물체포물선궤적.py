import turtle as t # 터틀
import math

tm = 0.3 # 시간 간격
ux = 0 # x 속도
uy = 0 # y 속도
dx = 0 # x 이동거리
dy = 0 # y 이동거리
g = 9.8 # 중력가속도 (g: 9.8)
velo = 0 # 속도
ang = 0 # 각도

# 포물선 운동을 하는 이동 궤적의 좌표마다 터틀의 흔적을 표시
def draw_pos(x, y):
    velo = t.numinput("입력", "속도 : ", 50, 10, 100) # 속도를 입력받아 velo에 대입(기본값:50, 최솟값 10, 최댓값:100)
    ang = math.radians(t.numinput("입력", "각도 : ", 45, 0, 360)) # 각도를 입력받아 ang에 대입(기본값:45, 최솟값:0, 최댓값:360)

    t.clearstamps() # 이전에 표시한 터틀 흔적을 모두 지움
    t.hideturtle() # 터틀을 숨김
    t.setpos(x,y) # 터틀의 위치를 x, y로 변경
    t.showturtle() # 터틀을 나타냄
    t.stamp() # 터틀을 찍음

    hl = -(t.window_height() / 2) # 윈도우 하단인 y축 위치를 계산하여 hl에 대입

    ux = velo * math.cos(ang) # x 속도 계산하여 ux에 대입
    uy = velo * math.sin(ang) # y 속도 계산하여 uy에 대입
    while True:
        uy = uy + (-1 * g) * tm # 중력가속도가 반영된 y 속도를 계산하여 uy에 대입
        dy = t.ycor() + (uy * tm) - (g * tm**2) / 2 # y 이동거리를 계산하여 dy에 대입
        dx = t.xcor() + (ux * tm) # x 이동거리를 계산하여 dx에 대입
        if dy > hl: # 만약 y이동거리가 윈도우 하단 y축 값보다 크다면
            t.goto(dx, dy) # 터틀의 위치를 dx, dy로 이동
            t.stamp() # 터틀을 찍음
        else: # 아니라면
            break # 루프 탈출

t.setup(600, 600) # 터틀 스크린 크기를 600, 600으로 설정
t.shape("circle") # 터틀 모양 설정
t.shapesize(0.3, 0.3, 0) # 터틀 크기를 0.3, 0.3으로 설정. 테두리는 설정안함(0)
t.penup() # 터틀 펜을 올림
s = t.Screen() # 터틀 스크린 생성
s.onscreenclick(draw_pos) # 터틀 스크린에서 마우스 클릭이 이루어지면 draw_pos() 골백 함수 호출
s.listen() # 터틀 스크린에서의 이벤트 확인

t.mainloop() # (파이썬 IDLE 사용을 하지 않는경우 창 유지를 위해 사용한다)