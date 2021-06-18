# 함수 반환값
def nyan():
    print('nyan')
    return 1

n = nyan()
print('return value:',n)
print('return value:'+str(n))

# 두 수의 평균을 구하는 avg() 함수로 평균 출력하기
def avg(a,b):
    return (a+b)/2

math = 50
english = 100
result = avg(math, english)
print('평균',result)
