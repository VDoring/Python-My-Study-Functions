# 전역변수 / 지역변수가 같은 이름으로 함수 내부에서 존재할 때

val = 3 # 전역변수 val 선언

def func1():
    lv1 = 1 # 지역변수 lv1 선언
    lv1 = lv1 + val # 지역변수 lv1 + "지역변수" val

    #val = 1  # 오류 발생!
              # 변수 val에 값을 대입하기 이전에 변수 val의 값 사용시 오류발생
              # 즉, 연산을 한 다음에 값 설정시 오류가 발생.
    print(lv1)

def func2(pv):
    lv2 = pv
    print(pv)

func1()
func2(2)
print(val) # 전역변수 val의 값