# 문자열을 입력받아 문자열의 길이를 구하고, 문자열의 첫 번째 문자, 두 번째 문자, 마지막 문자를 출력하기.

ustr = input("문자열 : ") # Python Programming 입력시
print("문자열 길이 : ", len(ustr)) # 18 출력됨
print("첫 번째 문자 : ", ustr[0]) # P 출력됨
print("두 번째 문자 : ", ustr[1]) # y 출력됨
print("마지막 문자 : ", ustr[len(ustr)-1]) # g 출력됨
                                           # ustr[len(ustr)-1]는 마지막 문자를 나타낸다.