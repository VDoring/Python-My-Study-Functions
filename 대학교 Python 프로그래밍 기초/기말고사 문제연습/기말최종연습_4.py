# 이름 입력받아 환영합니다 ~~님 출력하는 함수를 이용해 해당 메세지 출력하기
def welcome(name):
    print('환영합니다.',name,'님')

username = input('이름 :')
welcome(username)


# 문자열과 휫수를 매개변수로 전달받아 해당 휫수만큼 문자열 반복 출력
def print_str(userstr,n):
    for _ in range(n):
        print(userstr)

userstring = input('문자열 :')
user_n = int(input('휫수 :'))
print_str(userstring, user_n)