# https://wikidocs.net/14
# 리스트의 종류
# 리스트는 []으로 감싼다.
a = []
b = [1,3,5,7,9]
c = ['Hello', 'World']
d = [1, 2, 'Hello', 'World']
e = [1, 2, ['Life', 'is']]
print(a)
print(b)
print(c)
print(d)
print(e)


# 리스트의 인덱싱
# 리스트는 0에서 시작한다.
f = [1,2,3]

# 리스트의 요소들을 계산할 수 있다.
print('리스트 f의 0번째와 2번째를 더한값은', f[0] + f[2]) # 4

# -1,-2,-3등의 마이너스 값을 써도 리스트 사용 가능하다.
# (-1은 마지막 요솟값을 나타낸다.)
print(f[-1]) # 3 출력
print(f[-2]) # 2 출력
print(f[-3]) # 1 출력


# 리스트 안의 리스트
g = [1, 2, 3, ['a', 'b', 'c']]
print(g[0]) # 1 출력
print(g[-1]) # 마지막 요솟값 출력 (['a', 'b', 'c'])
print(g[3]) # 마지막 요솟값 출력 (['a', 'b', 'c'])
print(g[-1][0]) # 마지막 요소의 첫번째 값 출력 (a)
print(g[-1][1]) # 마지막 요소의 두번째 값 출력 (b)
print(g[-1][2]) # 마지막 요소의 세번째 값 출력 (c)

# 삼중 리스트
h = [1,2,['a','b',['Hello','World']]]
# (구조)
h = [
    1, 2, 
    [
        'a', 'b', 
        [
            'Hello',
            'World'
        ]
    ]
]
print(h[2][2][0]) # 2번째 요소의 2번째 요소의 첫번재 요소 출력 (Hello)

# 리스트의 슬라이싱
# 리스트를 나누는 것이다.
aa = [1,2,3,4,5]
print(aa[0:2]) # 리스트 0에서 1까지만 출력 ([1, 2])

# 리스트의 슬라이싱
bb = "12345" # 문자형 타입
print(bb[0:2]) # 문자열 0에서 1까지만 출력 (12)

cc = [1, 2, 3, 4, 5]
cc1 = cc[:2] 
print(cc1) # 리스트 0부터 1까지 출력 ([1, 2])
cc2 = cc[2:]
print(cc2) # 리스트 2부터 끝까지 출력 ([3, 4, 5])

# 중첩된 리스트에서 슬라이싱하기
dd = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(dd[2:5]) # 리스트 2부터 시작해 4까지 출력 ([3, ['a', 'b', 'c'], 4])
print(dd[3][:2]) # 리스트 3번째 요소안의 0번쨰부터 1번쨰 요소까지 출력 (['a', 'b'])

# 리스트 더하기(합치기)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2) # ([1, 2, 3, 4, 5, 6])

# 리스트 반복하기
print(list1 * 3) # 리스트 3번 반복 ([1, 2, 3, 1, 2, 3, 1, 2, 3])

# 리스트 길이구하기
print(len(list1)) # 3 출력

# 리스트 연산 오류 예시(문자열)
nlist = [1, 2, 3]
#print(nlist[2] + "Hello") #오류! nlist[2]에 저장된 값은 3(정수)이고, "Hello"는 문자열이기 때문.
print(str(nlist[2]) + "Hello") # 3Hello 출력

# 리스트에서 값 수정하기
k = [1, 2, 3]
print('기존 =', k[2])
k[2] = 4 # a[2]를 4로 바꿈
print('교체후 =', k[2])

# 리스트 요소 삭제하기
print(k) # [1, 2, 4] 출력
del k[2] # k[2] 삭제
print(k) # [1, 2] 출력
# del이란 함수는 객체를 놓아서 사용한다. (del 객체)
# del은 파이썬이 자체적으로 가지고 있는 삭제 함수이다.
# 이때 객체란 파이썬에서 사용되는 모든 자료형을 말한다.

# 리스트 요소 여러개 삭제하기(슬라이싱 활용)
l = [1, 2, 3, 4, 5]
print(l) # [1, 2, 3, 4, 5] 출력
del l[2:]
print(l) # [1, 2] 출력


# 리스트 관련 함수들 #
# 요소 추가(append)
m = [1, 2, 3]
m.append(4)
print(m) # [1, 2, 3, 4] 출력
m.append([5,6])
print(m) # [1, 2, 3, 4, [5, 6]] 출력

# 정렬(sort)
n = [1, 4, 3, 5, 2]
n.sort()
print(n) # [1, 2, 3, 4, 5] 출력
o = ['a', 'c', 'b']
o.sort()
print(o) # ['a', 'b', 'c'] 출력

# 뒤집기(reverse)
# 현재의 리스트를 반대순서로 바꿔주기만 할 뿐 정렬해주진 않는다.
p = ['a', 'c', 'b']
p.reverse()
print(p) # ['b', 'c', 'a'] 출력

# 리스트 요소 위치 값 반환(index)
q = [1,2,3]
print(q.index(3)) # 2 출력
print(q.index(1)) # 0 출력
#print(q.index(0)) 하면 오류가 발생한다.

# 요소 삽입(insert)
r = [1, 2, 3]
r.insert(0, 4) # r[0]위치에 4를 집어넣기
print(r) # [4, 1, 2, 3] 출력
r.insert(3, 5) # r[3]위치에 5 넣기
print(r) # [4, 1, 2, 5, 3] 출력 (기존 r[3]의 위치에 5를 삽입하면 3이 뒤로 밀려난다.)

# 요소 제거(remove)
s = [1, 2, 3, 1, 2, 3]
s.remove(3) # 3 한개 제거
print(s) # [1, 2, 1, 2, 3]

# 요소 끄집어내기(pop)
#리스트의 맨 마지막 요소를 돌려주고 그 요소는 리스트에서 삭제한다.
t = [1, 2, 3]
value = t.pop()
print(value) # 3 출력
print(t) # [1, 2] 출력
u = [1, 2, 3]
value2 = u.pop(1) # 1번째 요소를 돌려주고 그 요소를 리스트에서 삭제함
print(value2) # 2 출력
print(u) # [1, 3] 출력

# 리스트에 포함된 요소 x의 개수 세기(count)
v = [1, 2, 3, 1]
print(v.count(1)) # 1이라는 값이 리스트에 2개 들어있으므로 2를 반환(출력)한다. (2 출력)

# 확장(extend)
# 원래의 리스트에 더하게 된다. extend(x)의 x에는 리스트만 올 수 있다.
w = [1 ,2, 3]
w.extend([4,5])
print(w) # [1, 2, 3, 4, 5] 출력
temp = [6, 7]
w.extend(temp)
print(w) # [1, 2, 3, 4, 5, 6, 7] 출력