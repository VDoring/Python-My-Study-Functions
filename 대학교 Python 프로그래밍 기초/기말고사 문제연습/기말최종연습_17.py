# 리스트 조작_삭제
korean = ['가', '나',' 다', '라']
print(korean, len(korean)) # ['가', '나', ' 다', '라'] 4

del korean[2]
print(korean, len(korean)) # ['가', '나', '라'] 3

del korean[0:2]
print(korean, len(korean)) # ['라'] 1

korean.remove('라')
print(korean, len(korean)) # [] 0



# 소숫점 자리수 맞추기
value = 12345.458763
print('%.3f'%value) # 12345.459