def print19(st,ed):
    for i in range(st, ed+1):
        print(i, end = ' ')

s = int(input('시작 값:'))
e = int(input('끝 값:'))
if s < e:
    print19(s,e)
else:
    print('오류:변수s의 값이 e의 값보다 작아야 합니다! (시작 값이 끝 값보다 작아야 합니다!')