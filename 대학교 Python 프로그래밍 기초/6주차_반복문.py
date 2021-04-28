n = 1
sum = 0
while n <= 10:
    if n % 2 == 0: # 짝수일떄
        sum = sum + n
    n = n + 1
print('sum:', sum) # 30
                    # (2+4+6+8+10)


sum = 0
for i in range(1, 11, 2): # 1~10까지 범위가 정해지고, 2씩 증가하며 작동한다.
    sum = sum + i
print('sum:', sum) # 25

sum = 0
for i in range(9, -1, -2): # 9에서 0까지 가는데, -2씩 감소하며 작동한다.
    sum = sum + i
print('sum:', sum) # 25