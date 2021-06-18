# 유저가 가로, 세로 값 입력한 것을 바탕으로 사각형 그리기
import turtle as t

def rectangle_draw(col,row):
    for _ in range(2):
        t.forward(col)
        t.right(90)
        t.forward(row)
        t.right(90)

user_col, user_row = int(input('가로:')), int(input('세로:'))
rectangle_draw(user_col, user_row)
