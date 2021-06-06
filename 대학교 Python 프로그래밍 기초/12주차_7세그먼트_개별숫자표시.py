import turtle as t

s7seg_base = "7s10.gif"
s7seg_led = [ "7s-a.gif", "7s-b.gif", "7s-c.gif", "7s-d.gif", "7s-e.gif", "7s-f.gif", "7s-g.gif" ]

             # a b c d e f g
s7seg_num = [ [1,1,1,1,1,1,0], # 0
              [0,1,1,0,0,0,0], # 1
              [1,1,0,1,1,0,1], # 2
              [1,1,1,1,0,0,1], # 3
              [0,1,1,0,0,1,1], # 4
              [1,0,1,1,0,1,1], # 5
              [1,0,1,1,1,1,1], # 6
              [1,1,1,0,0,0,0], # 7
              [1,1,1,1,1,1,1], # 8
              [1,1,1,1,0,1,1] ] # 9

# s7seg_img 리스트 내에서 누른 숫자에 해당하는 7세그먼트 형식의 숫자 이미지를 터틀 모양으로 변경하고 해당 터틀의 흔적을 남기는 함수
def disp_num(k):
    t.shape(s7seg_base) # s7seg_base 형태(모든 단자의 개별 LED가 꺼진 형태)로 터틀 모양 변경
    t.stamp() # 터틀의 흔적 남김
    if k < 10: # 만약 k가 10보다 작으면
        for i in range(7): # a부터 g에 해당하는 0부터 6까지 반복
            if s7seg_num[k][i] == 1: # 만약 s7seg_num[k][i]의 값이 1이면
                t.shape(s7seg_led[i]) # s7seg_led[i]의 모양으로 터틀 모양 변경
                t.stamp() # 터틀의 흔적을 남김

def key_0():
    disp_num(0) # 숫자 키에 해당하는 함수 호출
def key_1():
    disp_num(1)
def key_2():
    disp_num(2)
def key_3():
    disp_num(3)
def key_4():
    disp_num(4)
def key_5():
    disp_num(5)
def key_6():
    disp_num(6)
def key_7():
    disp_num(7)
def key_8():
    disp_num(8)
def key_9():
    disp_num(9)
def key_10():
    t.clearstamps()
    disp_num(10)

t.setup(400, 400) # 터틀 스크린 크기 설정
s = t.Screen() # 터틀 스크린 생성
t.hideturtle() # 터틀 숨김
t.speed(0) # 터틀 속도 설정(아주 빠름)

s.addshape(s7seg_base) # s7seg_base 형태 이미지를 터틀 모양으로 등록
for i in range(7): # 0부터 6까지 반복하며 s7seg_led 리스트의 개별 단자 이미지를 터틀 모양으로 등록
    s.addshape(s7seg_led[i])
disp_num(10) # disp_num(10) 함수 호출

# 0~9키가 눌러지면 key_0()~key_9() 콜백 함수 호출
s.onkeypress(key_0, '0')
s.onkeypress(key_1, '1')
s.onkeypress(key_2, '2')
s.onkeypress(key_3, '3')
s.onkeypress(key_4, '4')
s.onkeypress(key_5, '5')
s.onkeypress(key_6, '6')
s.onkeypress(key_7, '7')
s.onkeypress(key_8, '8')
s.onkeypress(key_9, '9')

# 누르고 있던 키를 놓으면 key_10() 콜백 함수 호출
s.onkeyrelease(key_10, '0')
s.onkeyrelease(key_10, '1')
s.onkeyrelease(key_10, '2')
s.onkeyrelease(key_10, '3')
s.onkeyrelease(key_10, '4')
s.onkeyrelease(key_10, '5')
s.onkeyrelease(key_10, '6')
s.onkeyrelease(key_10, '7')
s.onkeyrelease(key_10, '8')
s.onkeyrelease(key_10, '9')
s.onkeyrelease(key_10, '10')

s.listen() # 터틀 스크린에서의 이벤트 확인

t.mainloop()