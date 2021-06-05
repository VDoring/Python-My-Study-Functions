# 위로 방향키와 아래로 방향키를 이용하여 80도 미만은 5도씩
# 80도 이상은 10도 간격으로 온도를 조절한다.
# 온도의 변화에 맞추어 온도가 80도 미만이면 "정상" 글자와 함께 백색 원을 터틀 스크린에 표시하고,
# 120도 미만이면 "주의" 글자와 청색 원, 120도 이상이면 "화재" 글자와 적색 원을 표시한다.

import turtle as t

color_status = ['white', 'blue', 'red'] # 상태에 해당하는 색상
alert_status = ['정상', '주의', '화재'] # 화재경보기 상태
tempc = 50 # 현재 온도 표시. 50은 기본값

# 온도에 따른 상태를 나타내는 문자열과 색상 원 표시하는 함수
def check_fire():
    if tempc < 80: # 80도보다 작을시
        status = 0 # 화재경보기 상태: 정상
    elif tempc < 120: # 120도보다 작을시
        status = 1 # 화재경보기 상태: 주의
    else: # 120도가 넘으면
        status = 2 # 화재경보기 상태: 화재

    t.clear() # 이전에 표시한 터틀 흔적을 모두 지움
    t.home() # 터틀의 위치를 초기 위치로 변경
    t.pendown() # 펜을 내림
    t.fillcolor(color_status[status]) # color_status 리스트에 있는 색 리스트 중 하나 저장
    t.begin_fill() # 원 그리기 준비
    t.circle(20) # 원 크기를 20으로 지정
    t.end_fill() # 원 그리기
    t.penup() # 펜을 올림
    t.goto(-22, 50) # 상태, 온도 출력을 위해 -22, 50 위치로 이동
    t.write('%s : %d' %(alert_status[status], tempc)) # color_status 리스트 값과 온도값 출력

# 온도를 5도 또는 10도 증가하고. check_fire() 호출하는 함수
def keyUp():
    global tempc
    if tempc < 80: # 온도가 80보다 작으면
        tempc = tempc + 5 # 온도 5도 증가
    else: # 온도가 80보다 크면
        tempc = tempc + 10 # 온도 10도 증가
    check_fire() # check_fire() 함수 호출

# 온도를 5도 또는 10도 감소하고. check_fire() 호출하는 함수
def keyDown():
    global tempc
    if tempc < 80: # 온도가 80보다 작으면
        tempc = tempc - 5 # 온도 5도 감소
    else: # 온도가 80보다 크면
        tempc = tempc - 10 # 온도 10도 감소
    check_fire() # check_fire() 함수 호출

t.setup(300, 300) # 터틀 스크린 크기를 300, 300으로 설정
s = t.Screen() # 터틀 스크린 생성
t.hideturtle() # 터틀 숨김
t.speed(0) # 터틀의 속도 설정: 아주 빠름(0)
check_fire() # check_fire() 호출

s.onkey(keyUp, 'Up') # 위 방향키가 눌러지면 keyUp() 호출
s.onkey(keyDown, 'Down') # 아래 방향키가 눌러지면 keyDown() 호출
s.onkey(s.bye, 'q') # q 키가 눌러지면 터틀 종료
s.listen() # 터틀 스크린에서 이벤트 확인

t.mainloop()