# 숫자 처리 함수

# abs(-5)
# -5의 절댓값을 구한다.
print(abs(-5)) # 5

# pow(4,2)
# 4의 2승을 구한다.
print(pow(4,2)) # 16

# max(5, 12)
# 5와 12중 더 큰 수를 반환한다.
print(max(5, 12)) # 12

# min(5, 12)
# 5와 12중 더 작은 수를 반환한다.
print(min(5, 12)) # 5

# round(3.14)
# 반올림을 해준다. 소숫점 값에 따라 버리거나 올려준다.
print(round(3.14)) # 3
print(round(4.85)) # 5


from math import *  # math 라이브러리에 있는 모든 것을 사용하겠다는 의미.

# floor(4.99)
# 소수점 내림.
print(floor(4.99)) # 4

# ceil(3.14)
# 소수점 올림
print(ceil(3.14)) # 4

# sqrt(16)
# 제곱근
print(sqrt(16)) # 4