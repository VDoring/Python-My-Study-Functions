sec = int(input("sec를 입력하세요 : "))
min = sec // 60
remainder = sec % 60
print("입력하신 값은", str(sec) + "초 입니다.")
print("이 값은", str(min) + "분", str(remainder) + "초 입니다.")
