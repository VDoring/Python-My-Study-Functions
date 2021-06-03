import turtle as t

s7seg_img = [ "7s0.gif", "7s1.gif", "7s2.gif", "7s3.gif", "7s4.gif", "7s5.gif", "7s6.gif", "7s7.gif", "7s8.gif", "7s9.gif", "7s10.gif" ]

# s7seg_img 리스트 내에서 누른 숫자에 해당하는 7세그먼트 형식의 숫자 이미지를 터틀 모양으로 변경하고 해당 터틀의 흔적을 남김.
def disp_num(k):
    t.shape(s7seg_img[k]) # s7seg_img 리스트에서 k 위치의 숫자 이미지를 터틀 모양으로 변경
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
    disp_num(10)

t.setup(400, 400) # 터틀 스크린 크기 설정
s = t.Screen() # 터틀 스크린 생성
t.hideturtle() # 터틀 숨김
t.speed(0) # 터틀 속도 설정(아주 빠름)

for i in range(11): 
    s.addshape(s7seg_img[i])

disp_num(10)

s.onkey(key_0, "0")
s.onkey(key_1, "1")
s.onkey(key_2, "2")
s.onkey(key_3, "3")
s.onkey(key_4, "4")
s.onkey(key_5, "5")
s.onkey(key_6, "6")
s.onkey(key_7, "7")
s.onkey(key_8, "8")
s.onkey(key_9, "9")
s.onkey(key_10, "r")
s.listen()

t.mainloop()