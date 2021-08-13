# 문자열 처리 함수

python = 'Python is Amazing' # 대문자가 포함된 문자열
print(python.lower()) # 전체 소문자 출력. python is amazing 출력됨
print(python.upper()) # 전체 대문자 출력. PYTHON IS AMAZING 출력됨
print(python[0].isupper()) # 첫 글자가 대문자일 경우 True 출력. True 출력됨
print(python[0].islower()) # 첫 글자가 소문자일 경우 Ture 출력. False 출력됨
print(len(python)) # 띄어쓰기 포함 문자열 길이 출력
print(python.replace('Python', 'java')) # 문자열에서 Python부분을 찾아 Java로 바꾼다.
                                        # java is Amazing 출력됨

index = python.index('n') # 문자열에서 n이 몇 번째 자리에 있는지 출력
print(index) # 5 출력됨

index = python.index('n', index + 1) # 문자열에서 두 번째 n의 자리수를 출력
print(index) # 15 출력됨

print(python.find('n')) # 문자열에서 n 문자의 위치를 출력한다. 5 출력됨
print(python.find('Good')) # 문자열에 없는 문자를 찾는경우 -1 출력. -1 출력됨
# print(python.index('Good')) # 문자열에 없는 문자를 찾는경우 오류남(프로그램 종료됨)

print(python.count('n')) # 문자열에서 n이 몇 번 나왔는지 출력한다.