#반환값 처리
# 지역변수를 전체 함수에서 사용할 수 있는가?
# 지역변수 = 함수 내부에 선언된 변수

'''
def plus(x1, x2):
    result = x1 + x2
    return result

sum = plus(10, 20)

print(sum)
'''

#전역변수에 대해 알아보자
# x1, x2를 전체 프로그램 변수(전역변수)로 사용하기
# 전역변수를 함수에서 수정해서 사용하고 싶으면
# global 명령어를 사용해야함
'''
def minus():
    global result
    result = x1 - x2
    return

result = 0
x1 = 10
x2 = 20
minus()

print(result)
'''

#함수에서 다른 함수를 호출할 수 있음
def plus(x1, x2):
    result = x1 + x2
    return result

def minus(x1, x2):
    result = x1 - x2
    return result

def calculator(x1, x2, operator):
    if operator == "+":
        return plus(x1, x2)
    if operator == "-":
        return minus(x1, x2)

grade1 = 50
grade2 = 60

print(calculator(grade1, grade2, "+"))
print(calculator(grade1, grade2, "-"))
