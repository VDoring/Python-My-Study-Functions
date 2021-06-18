# print() 함수를 이용하여 학번과 이름을 2회 출력하기
print(12345678,"가나다")
print(12345678,"가나다")

# for문 이용해 "
for _ in range(2):
    print(12345678,"가나다")

# 학번과 이름을 출력하는 sn()함수를 만든 후 "
def sn():
    print(12345678,"가나다")
sn()
sn()

# for문 이용해 sn()함수를 "
for _ in range(2):
    sn()

# 함수에 매개변수 넣기
def pos(x,y):
    print('Your position is',x,y)

pos(100,200)


# 사용자로부터 계산할 단을 입력받아 해당 구구단의 단을 계산하여 출력하기
def gugudan(dan):
    for i in range(10):
        print(dan*i)

user_dan = int(input())
gugudan(user_dan)