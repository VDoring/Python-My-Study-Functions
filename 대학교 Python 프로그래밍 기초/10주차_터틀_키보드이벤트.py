# onkey(콜백함수, key이름)
# 키를 누르고 띄는 이벤트 처리

# onkeypress(콜백함수, key이름)
# 키를 누르고 있는 이벤트 처리

# onkeyrelease(콜백함수, key이름)
# 누르고 있던 키를 놓는 이벤트 처리

import turtle as t

def print_key(char):
    print(char, end='')

def key_a():
    print_key('aa')

def key_sp():
    print_key('s_')

def key_sr():
    print_key('S^')

s = t.Screen()
s.onkey(key_a, 'a') # onkey()에 의해 aa 출력
s.onkeypress(key_sp, 's') # onkeypress()에 의해 s_ 출력
s.onkeyrelease(key_sr, 's') # onkeyrelease()에 의해 s^ 출력
s.onkey(s.bye, 'q')
s.listen()

t.mainloop()