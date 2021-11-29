heroes = ["아이언맨","토르","헐크","스파이더맨","캡틴"]

lists = [1, 1.5, 5, 4, 2]

for r in lists:
    area = 3.14 * r * r
    print("반지금", str(r) + "의 부피는", str(area))

heroes.sort()
print(heroes)

heroes.sort(reverse=True)
print(heroes)



#n명의 회원을 가입 시킬수 있음
guest_id = []
guest_pwd = []

print("회원가입")
while True:
    id = input("아이디를 입력하세요.)")
    if id in guest_id:
        print("등록된 아이디 입니다.")
    else:
        guest_id.append(id)
        pwd = input("비밀번호를 입력하세요.)")
        guest_pwd.append(pwd)

    cont_sign = input("회원가입을 계속 하시겠습니까? 그만:0, 계속:아무키")
    if cont_sign == "0":
        break

    print(guest_id)
    print(guest_pwd)
