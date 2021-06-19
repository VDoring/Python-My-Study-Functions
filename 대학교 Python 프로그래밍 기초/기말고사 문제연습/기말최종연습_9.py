# 입력받은 값대로 사각형을 그리고 터틀화면에 문장 출력하기
import turtle as t

def drawBox(x,y):
    turtlemsg = '가로'+str(x)+'세로'+str(y)+'인 사각형의 넓이 ='+str(x*y)  # 터틀 표시 문장 #
    t.write(turtlemsg)
    
    for _ in range(2):
        t.forward(x)
        t.right(90)
        t.forward(y)
        t.right(90)

x = int(input('가로:'))
y = int(input('세로:'))
drawBox(x,y)