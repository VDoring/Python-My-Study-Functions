fruit = []
fruit.append('사과')
fruit.append('배')
fruit.append('감')
print(fruit) # ['사과', '배', '감']

for i in range(len(fruit)):
    print(i, fruit[i]) # 0 사과
                       # 1 배
                       # 2 감

fruit.insert(2, '딸기')
print(fruit) # ['사과', '배', '딸기', '감']

for i in range(len(fruit)):
    print(i, fruit[i]) # 0 사과
                       # 1 배
                       # 2 딸기
                       # 3 감