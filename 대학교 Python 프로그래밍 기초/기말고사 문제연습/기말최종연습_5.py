# 문자와 휫수를 매개변수로 전달받아 휫수만큼 문자를 반복하여 출력하는 dispch() 함수 선언하고 출력하기
def dispch(character, n):
    for _ in range(n):
        print(character, end='')

user_char = input('문자 :')
user_n = int(input('휫수 :'))
dispch(user_char,user_n)