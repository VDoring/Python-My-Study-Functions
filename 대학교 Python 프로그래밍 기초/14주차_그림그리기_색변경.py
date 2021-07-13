import turtle as t

draw_action = 1
oldx = 0
oldy = 0

# 딕셔너리를 통한 펜의 색상 지정 및 초기 펜 색상 설정
pen_color_name = {0:"Black", 1:"Red", 2:"Green", 3:"Blue"}
pen_color = 0

def new_clear():
    global draw_action
    global oldx
    global oldy
    t.clear()
    t.pensize(1)
    t.pendown()
    draw_action = 1
    oldx = 0
    oldy = 0

def draw(x,y):
    global oldx
    global oldy

    if draw_action == 1: # 선 그리기
        t.goto(x,y)
        oldx = x
        oldy = y
    elif draw_action == 2: # 삼각형 그리기
        t.goto(x, oldy)
        t.goto((x+oldx)//2,y)
        t.goto(oldx,oldy)
    elif draw_action == 3: # 사각형 그리기
        t.goto(x,oldy)
        t.goto(x,y)
        t.goto(oldx,y)
        t.goto(oldx,oldy)
    elif draw_action == 4: # 원형 그리기
        t.circle(-((x-oldx))//2)

def drag(x,y):
    if draw_action == 1:
        draw(x,y)

def move(x,y):
    global oldx
    global oldy
    penstatus = t.isdown()
    t.penup()
    t.goto(x,y)
    if penstatus == True:
        t.pendown()
    oldx = x
    oldy = y

def key_l():
    global draw_action
    draw_action = 1
def key_t():
    global draw_action
    draw_action = 2
def key_r():
    global draw_action
    draw_action = 3
def key_c():
    global draw_action
    draw_action = 4
def key_n():
    new_clear()
def key_u():
    t.penup()
def key_d():
    t.pendown()
def key_k(): # k 키를 누를 때마다 펜 색상 변경
    global pen_color
    pen_color = pen_color + 1
    if pen_color > 3:
        pen_color = 0
    t.color(pen_color_name[pen_color])
def key_1():
    t.pensize(1)
def key_3():
    t.pensize(3)
def key_5():
    t.pensize(5)

t.setup(600,600)
s = t.Screen()
t.shapesize(2)
t.speed(0)
t.left(900)
new_clear()

t.ondrag(drag)
s.onkey(key_l, "l")
s.onkey(key_t, "t")
s.onkey(key_r, "r")
s.onkey(key_c, "c")
s.onkey(key_n, "n")
s.onkey(key_u, "u")
s.onkey(key_d, "d")
s.onkey(key_k, "k") # k 키 -> 펜의 색상 지정
s.onkey(key_1, "1")
s.onkey(key_3, "3")
s.onkey(key_5, "5")

s.onscreenclick(draw, 1) # 마우스 왼쪽 -> 그리기
s.onscreenclick(move, 3) # 마우스 오른쪽 -> 좌표 이동
s.listen()

# t.mainloop() #(Visual Studio code 터틀이 꺼지지 않게 해주는 코드)