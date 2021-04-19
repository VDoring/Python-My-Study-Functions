a = int(input('첫번째 수를 입력하세요: '))
sign = input('부호를 입력하세요: ')
b = int(input('두번째 수를 입력하세요: '))

if sign == '+':
    print(a, '+', b, '=', a+b)
elif sign == '-':
    print(a, '-', b, '=', a-b)
elif sign == '*':
    print(a, '*', b, '=', a*b)
elif sign == '/':
    print(a, '/', b, '=', a/b)