user_id = "student_yhj"
user_pw = "pythonstudy"

guest_id = input("id를 입력하세요: ")
guest_pw = input("pw를 입력하세요: ")

if guest_id == user_id:
    if guest_pw == user_pw:
        print("환영합니다")
    else:
        print("올바르지 않은 pw입니다.")
else:
    print("올바르지 않은 id입니다.")
