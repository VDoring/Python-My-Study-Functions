print("내 나이는 " + str(20) + "입니다")
print("원주율은 " + str(3.14) + "입니다")

price = 50000
item= "노트북"
print("%s의 가격은 %s 입니다." % (item, price))       # 노트북의 가격은 50000 입니다.
print("{}의 가격은 {} 입니다.".format(item, price))   # 노트북의 가격은 50000 입니다.
print("{0}의 가격은 {1} 입니다.".format(item, price)) # 노트북의 가격은 50000 입니다.

greeting = "Hello World"
#           012345678910
print(greeting[3:5])
print(greeting[0:5])
print(greeting[6:11])
