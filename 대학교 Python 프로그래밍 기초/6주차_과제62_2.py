sign = input()

while sign=='+' or sign=='-' or sign=='*' or sign=='/':
    # a 랑 b 따로 입력할경우 #
    a = int(input())
    b = int(input())
    
    # 'a b' 같이 입력할경우 #
    # a, b = map(int,input().split())

    if sign=='+':
        print(a+b)
    if sign=='-':
        print(a-b)
    if sign=='*':
        print(a*b)
    if sign=='/':
        print(a/b)

    sign = input()
