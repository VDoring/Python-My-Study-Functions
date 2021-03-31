# 수식(expression)
# 피연산자들과 연산자의 조합으로 구성.
# 피연산자(operand) : 연산의 대상이 되는 것
# 연산자(operator) : 어떤 연산을 나타내는 기호 (산술 연산자, 관계 연산자, 논리 연산자, 비트 연산자 등)

x = int(input('정수를 입력: '))
print(x)

# 연산자 종류
one = 10 / 3 # 나눗셈(실수)
two = 10 // 3 # 나눗셈(정수)
tre = 10 % 3 # 나머지
print(one) # 3.3333333333333335
print(two) # 3
print(tre) # 1


# 정수를 입력받아 필요한 동전 개수 구하기
needmoney = int(input('금액: '))
x500 = needmoney // 500
x100 = needmoney % 500
x100 = x100 // 100
print('500원:',x500,'100원:',x100)