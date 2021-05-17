import turtle as t

# 떨어지는 물체의 이동 궤적 좌표마다 터틀의 흔적을 표시하는 함수.
# (x,y는 유저가 마우스로 누른 좌표이다.)
def draw_pos(x, y):
    t.clear() # 화면 클리어
    t.setpos(x, y) # 터틀 위치를 x,y로 설정 (유저가 클릭한 위치로 이동)
    t.stamp() # 터틀의 흔적을 남김 (점을 찍어 표시)

    hl = -(t.window_height() / 2) # 화면의 하단부분 y축 위치 계산 (이 코드에서는 -300)

    tm = 0 # 시간 변수 초기화
    while True:
        d = (9.8 * tm**2) / 2 # 이동 거리 계산
        ny = y - int(d) # y좌표에서 이동거리를 뺀다
        if ny > hl: # 만약 터틀화면 하단부분(y축)보다 위에 있을때
            t.goto(x, ny) # 터틀의 위치를 x,ny로 이동
            t.stamp() # 터틀의 흔적을 남김
            tm = tm + 0.3 # tm값 1 증가
        else: #만약
            break

t.setup(500, 600) # 터틀 GUI 화면 크기 설정
t.shape("circle") # 터틀 모양을 원으로 설정
t.shapesize(0.3, 0.3, 0) # 터틀 크기를 0.3,0.3으로 설정. 테두리는 설정하지 않음(0)
t.penup() # 터틀 펜을 올림
s = t.Screen() # 터틀 스크린 생성
s.onscreenclick(draw_pos) # 터틀 화면에 마우스 클릭 시 draw_pos() 콜백 함수 호출
s.listen() # 터틀 스크린에서 이벤트 확인

t.mainloop() # (파이썬 IDLE에서 실행하는 경우가 아닌 경우 터틀 화면이 꺼지지 않게한다)