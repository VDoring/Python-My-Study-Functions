def addition(x,y):
    print(a+b)

def subtract(x,y):
    print(a-b)

def multiply(x,y):
    print(a*b)

def divide(x,y):
    print(a/b)

sign = input()

while sign=='+' or sign=='-' or sign=='*' or sign=='/':
    # a 랑 b 따로 입력할경우 #
    a = int(input())
    b = int(input())
    
    # 'a b' 같이 입력할경우 #
    # a, b = map(int,input().split())

    if sign=='+':
        addition(a,b)
    elif sign=='-':
        subtract(a,b)
    elif sign=='*':
        multiply(a,b)
    elif sign=='/':
        divide(a,b)

    sign = input()
