opnd1 = int(input('피연산자1: '))
if int(opnd1) >= 100 and int(opnd1) <= 999:
    opnd2 = int(input('피연산자2: '))

    if opnd2 >= 1 and opnd2 <= 9:
        hundreds = opnd1 - (opnd1 % 100)
        tens = opnd1 % 100 - (opnd1 % 10)
        units = opnd1 % 10

        print(opnd1, '*', opnd2)
        print('=', '(', hundreds, '+', tens, '+', units, ')', '*', opnd2)
        print('=', hundreds, '*', opnd2, '+', tens, '*', opnd2, '+', units, '*', opnd2)
        print('=', hundreds * opnd2, '+', tens * opnd2, '+', units * opnd2)
        print('=', opnd1 * opnd2)

    else:
        print('opnd2 입력 오류')
else:
    print('opnd1 입력 오류')