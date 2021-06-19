# 키보드의 숫자 1,2,3중 아무거나 누르면 그것이 출력된다.

import turtle as t

def print_dight(n): # 숫자 출력
    print(n, end='')

def key_1():
    print_dight(1)
def key_2():
    print_dight(2)
def key_3():
    print_dight(3)

s = t.Screen()
s.onkey(key_1, '1')
s.onkey(key_2, '2')
s.onkey(key_3, '3')
s.listen()

t.mainloop()