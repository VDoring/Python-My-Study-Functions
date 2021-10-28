# list 실습, 영웅 추가하기

list1 = ["아이언맨", "토르", "헐크"]
#            0          1       2
print(list1[2])

list2 = []
list2.append("아이언맨")
list2.append("토르")
list2.append("헐크")

print(list2)

print(list2[2])


heroes = ["아이언맨", "토르", "헐크", "스파이더맨", "캡틴"]
print(heroes)

print(heroes[0:3])
print(heroes[:3])
print(heroes[3:])
print(heroes[:])
print(heroes[1:3])

heroes_two = heroes[1:3]
print(heroes_two)
