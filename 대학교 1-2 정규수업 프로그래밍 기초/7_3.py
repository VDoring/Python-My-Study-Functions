# 함수는 스스로를 호출할 수 있음 = 재귀함수
# n을 입력받으면 1부터 n까지 출력하는 함수
# for문 or while문을 이용한 case
# 함수만 이용해서 1부터 n까지 출력


n = 10
for i in range(10):
    print(i+1)


# 작은 수에서 큰 수로 증가하도록 수정
# 1에서 멈춰야함

def print1_to_n(n): # 10
    if n < 1:
        return
    print1_to_n(n-1) # 9
    print(n)


print1_to_n(10)


# 1~n 출력하는 문제
# 1~n 재귀함수로 다를수있음
# 1~n 곱하는 문제도 가능
n = 4  # 1*2*3*4 = 24

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

print(factorial(n))

'''
factorial(n)
= n * factorial(n-1)

factorial(4)
= 4 * factorial(3)
= 4 * 3 * factorial(2)
= 4 * 3 * 2 *factorial(1)
'''
