# 문자열을 입력받아 for문을 이용하여 개별 문자로 출력해보자.
# 그리고 for문을 이용하여 입력받은 문자열의 역순으로 개별 문자를 출력해보자.

ustr = input("문자열 : ") # Python Programming 입력시

print("개별 문자 출력 : ", end="")
for i in range(len(ustr)):
    print(ustr[i], end="") # Python Programming 출력됨
print("")

print("역순 개별 문자 출력 : ", end="")
for i in range(len(ustr)-1, -1, -1): # gnimmargorP nohtyP 출력됨
                                     # 마지막문자(len(ustr)-1) 에서 처음문자(0)으로 반복할때마다 -1하며 작동
     print(ustr[i], end="")
print("")