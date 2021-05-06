# 랜덤함수

from random import *  # random 라이브러리에 있는 모든것들을 사용

print(random()) # 난수 생성. 실행시마다 다른 값 나옴
                # 0.0 이상 ~ 1.0 미만

print(random() * 10) # 0.0 이상 ~ 10.0 미만

print(int(random() * 10)) # 0 ~ 10 미만. 소수점 제외한 값이 나온다.

print(int(random() * 10) + 1) # 1 ~ 10 '이하'

print(int(random() * 45) + 1) # 1 ~ 45 '이하'

print(randrange(1, 46)) # 1 ~ 45 이하. 편리한 함수 1

print(randint(1, 45)) # 1 ~ 45 이하. 편리한 함수 1