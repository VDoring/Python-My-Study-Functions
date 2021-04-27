# 리스트의 요소 값은 0부터 시작한다.

list1 = [1,2,3,4,5]
list2 = ['a','b','c']
list3 = [1, 'a', 'abc', [1, 2, 3]]

print(list1[0]) # 1
print(list1[1]) # 2
print(list2[1]) # b
print(list3[2]) # abc

list1[1] = 30
print(list1) # [1, 30, 3, 4, 5]

list2[1] = 'abc'
print(list2) # ['a', 'abc', 'c']

# append()
list1.append(7)
print(list1) # [1, 30, 3, 4, 5, 7]

list2.append('d')
print(list2) # ['a', 'abc', 'c', 'd']

# insert()
list1.insert(2, 50) # 2번쨰 요소에 50이란 값 추가. (단, 리스트는 0부터 시작함을 유의)
print(list1) # [1, 30, 50, 3, 4, 5, 7]


# 리스트와 for를 같이 사용하기
sum = 0
for i in [1,2,3,4,5]:
    sum = sum + i
print('모두 더한 값: ', sum) # 모두 더한 값:  15

sum = 0
for i in [1,2,3,4,5]:
    sum = sum + i
    print('i의 값:', i, ', sum의 값:', sum)
print('모두 더한 값: ', sum)
# i의 값: 1 , sum의 값: 1
# i의 값: 2 , sum의 값: 3
# i의 값: 3 , sum의 값: 6
# i의 값: 4 , sum의 값: 10
# i의 값: 5 , sum의 값: 15
# 모두 더한 값:  15