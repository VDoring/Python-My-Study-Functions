import turtle as t

robot_fn = "robotic_vacuum.gif"
rx = []
ry = []
move_cnt = 0

# 매개변수 값에 따라 저장된 모든 지점에 대해 해당 동작을 수행함
def move_robot(action):
    t.clear() # 터틀 흔적 지우기
    if action == 0:
        for i in range(move_cnt): # 0부터 move_cnt-1까지 반복하면서 rx[i], ry[i]로 이동
            t.goto(rx[i], ry[i])
    elif action == 1:
        for i in range(move_cnt-1, -1, -1): # move_cnt-1부터 0까지 반복하면서 rx[i], ry[i]로 이동
            t.goto(rx[i], ry[i])
    elif action == 2:
        t.goto(rx[move_cnt-1], ry[move_cnt-1]) # rx[move_cnt-1], ry[move_cnt-1]로 이동
    elif action == 3:
        t.goto(rx[0],ry[0]) # rx[0],ry[0]로 이동
    t.penup() # 터틀 펜을 올림

# 클릭한 지점들을 저장함
def clicked(x, y):
    global move_cnt
    move_cnt += 1 # move_cnt의 값 1 증가
    rx.append(x) # rx에 x좌표를 추가
    ry.append(y) # ry에 y좌표를 추가

# 저장된 모든 지점을 지움
def list_clear():
    global move_cnt
    del rx[1:move_cnt] # rx에서 1부터 move_cnt까지의 값을 모두 삭제
    del ry[1:move_cnt] # ry에서 1부터 move_cnt까지의 값을 모두 삭제
    move_cnt = 1 # move_cnt의 값을 1로 설정

# 저장된 지점들을 순서대로 이동하기 위해 move_robot(0) 함수 호출
def key_SP():
    move_robot(0)

# 저장된 지점들을 역순으로 복귀하기 위해 move_robot(1) 함수 호출
def key_BS():
    move_robot(1)

# 최단 거리로 마지막 지점으로 이동하기 위해 move_robot(2) 함수 호출
def key_s():
    move_robot(2)

# 최단 거리로 처음 지점으로 복귀하기 위해 move_robot(3) 함수 호출
def key_r():
    move_robot(3)

# 저장된 모든 지점을 지우기 위해 list_clear() 함수 호출
def key_e():
    list_clear()

t.setup(600, 600) # 터틀 스크린 크기를 600, 600으로 설정
s = t.Screen() # 터틀 스크린 생성
t.hideturtle() # 터틀 숨김

s.addshape(robot_fn) # robot_fn 형태 이미지를 터틀 모양으로 등록
t.shape(robot_fn) # robot_fn 형태 이미지로 터틀 모양 변경
t.speed(6) # 터틀 속도 보통(6)으로 성정
t.penup() # 터틀 펜 올림
clicked(-265, 265) # 터틀 초기 위치 등록 위해 clicked(-265, 265) 함수 호출
t.showturtle() # 터틀을 나타냄

s.onkey(key_SP, 'space') # 스페이스 키가 눌리면 key_SP() 콜백 함수 호출
s.onkey(key_BS, 'BackSpace') # (밑도 동일)
s.onkey(key_s, 's')
s.onkey(key_r, 'r')
s.onkey(key_e, 'e')
s.onscreenclick(clicked) # 마우스 클릭이 감지되면 clicked() 콜백 함수 호출
s.listen() # 터틀 스크린에서 이벤트 확인

t.mainloop()