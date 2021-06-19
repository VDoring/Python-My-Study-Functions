# 교수추천문제
# 1
user_str = 'Python Programming'
print('문자열 길이:', len(user_str))
print('첫 번째 문자:',user_str[0])
print('두 번째 문자:',user_str[1])
print('마지막 문자:', user_str[-1])


# 2
user_str = 'Python Programming'
print('개별 문자 출력: ', end='')
for i in user_str:
    print(i, end='')
print()

print('역순 개별 문자 출력: ', end='')
for i in range(len(user_str)-1, -1, -1):
    print(user_str[i], end='')
print()

# 또는
print('역순 개별 문자 출력: ', end='')
for i in reversed(user_str):
    print(i,end='')
print()


# 3
score = 59
if score > 100 or score < 0:
    print('입력 가능한 점수 범위는 0~100 입니다.')
else:
    print(score,': ', end='')
    if score >= 90:
        print('A')
    elif score <= 89 and score >= 80:
        print('B')
    elif score <= 79 and score >= 70:
        print('C')
    elif score <= 69 and score >= 60:
        print('D')
    else:
        print('E')


# 4
score = 89
if score > 100 or score < 0:
    print('입력 가능한 점수 범위는 0~100 입니다.')
grade = {10:'A',9:'A',8:'B',7:'C',6:'D',5:'E',4:'E',3:'E',2:'E',1:'E',0:'E'}
print(score,':',grade[score//10])