# 1
sstr = 'python'
for i in range(len(sstr)):
    print(sstr[0:i+1])
#p
#py
#pyt
#pyth
#pytho
#python 출력됨


# 2
sstr = 'python'
for i in range(len(sstr)):
    print('%6s'%sstr[0:i+1])
#     p
#    py
#   pyt
#  pyth
# pytho
#python


# 3
sstr = 'python'
for i in range(len(sstr)-1,-1,-1): # 5부터 0까지 -1씩 반복한다. 이 값은 i에 저장된다.
    print(sstr[i:len(sstr)]) # 5부터 5까지 출력.. 4부터 5까지 출력.. 3부터 5까지 출력..

# n
# on
# hon
# thon
# ython
# python



# 문자열 입력받을때 무엇으로 구성되어있는지 확인
user_str = '123zbc' # 입력값은 (숫자뿐이더라도) 일단 문자열로 간주한 상태에서 시작해야 한다. 그래야 isdight등의 함수를 사용할 수 있다.
if user_str.isdigit(): # 만약 숫자만으로 구성되어있다면
    print('숫자로 구성된 문자열')
elif user_str.isalpha(): # 만약 문자만으로 구성되어있다면
    print('문자로 구성된 문자열')
elif user_str.isalnum(): # 만약 숫자와 문자 둘 다 있다면
    print('숫자/문자로 구성된 문자열')


# 리스트에 입력한 문자열들 저장한 후 아무것도 입력하지 않을시 리스트 값 출력하기
while True:
    data = []
    user_input = input('문자열 : ')
    if user_input == '':
        break
    else:
        data.append(user_input)
print(data)


# 문자열 중 특정 문자 찾기
user_str = 'NyanNyan'
if 'a' in user_str: # a가 user_str에 들어있다면
    print('문자열에 a가 들어있습니다')
else:
    print('문자열에 a가 들어있지 않습니다')
# 이 코드에서는 문자열에 a가 들어있습니다 가 출력됨


# 리스트 특정 요소 삭제하기
user_list = ['cat','dog','bee']
user_list.remove('dog')
print(user_list) # ['cat', 'bee']