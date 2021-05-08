import turtle
#turtle.shape("turtle")

def rectangle_draw(col,row):
    for _ in range(2):
        turtle.forward(col)
        turtle.right(90)
        turtle.forward(row)
        turtle.right(90)

column = int(input('가로 : '))
roww = int(input('세로 : '))
print('가로', column, '세로', roww, '인 사각형의 넓이 =', column * roww)
rectangle_draw(column,roww)