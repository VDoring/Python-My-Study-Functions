val = 3 # 전역변수 val 선언

def func1():
    lv1 = 1 # 지역변수 lv1 선언
    lv1 = lv1 + val # 지역변수 lv1 + 전역변수 val
    print(lv1) # 4 출력됨

def func2(pv): # 매개변수 pv 선언
    lv2 = pv # 지역변수 lv2 = 매개변수 pv
    print(pv) # 2 출력됨

func1()
func2(2)
print(val) # 전역변수 val의 값
           # 3 출력됨