def issn_check(issn):
    s = 0

    for i in range(8,1,-1):
        s = s + int(issn[8-i]) * i
    print('ISSN 1~7자리의 가중치 반영 합계 : %d' %s)

    t = s % 11
    chk = (11-t) % 10
    print('ISSN 1~7자리의 체크 기호 값 : %d' %chk)

    if chk == int(issn[7]):
        rst = 1
    else:
        rst = 0
    return rst


issn = input('ISSN 8자리(- 제외) : ')

if len(issn) == 8:
    rst = issn_check(issn)
    if rst == 1:
        print('ISSN 코드 : %s은(는) 검증되었습니다.' %issn)
    else:
        print('ISSN 코드 : %s은(는) 검증되지 않았습니다.' %issn)
else:
    print('ISSN 코드 입력은 -를 제외하고 8자리를 입력해주세요.')
