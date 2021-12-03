# dictionary 선언, 출력

bible = {'요한복음':256}
bible['시편'] = 50

print(bible)

number = {1:256}
number[2] = 50

print(number)

if 1 in number:
    print(number[1])
if 2 in number:
    print(number[2])
print(number.keys())
print(number.values())
if 3 in number:
    print(number[3])
