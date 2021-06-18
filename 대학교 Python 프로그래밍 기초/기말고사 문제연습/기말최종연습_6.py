# 거듭제곱 함수 만들어서 거듭제곱이 포함된 계산하기
def pow_xy(x,y):
    return x**y

gz = pow_xy(2,4)
print('3 * 2**4 + 5 =', 3 * gz + 5)


# 자연수를 입력하면 그 수까지 더한 값을 출력한다. 다만 여기서는 2를 입력하면 1~20까지 더한 수로 간주한다.
def one2n_sum1(n):
    sum = 0
    n *= 10
    for i in range(n+1):
        sum += i
    return sum
num = int(input('자연수 :'))
if num >= 0:
    result = one2n_sum1(num)
    print('1 --',str(num*10),'=',result)
else:
    print('입력된 수가 1보다 작습니다.')