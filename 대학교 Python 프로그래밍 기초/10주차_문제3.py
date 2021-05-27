# 0~100 사이의 점수를 입력받아 입력한 점수가 0~100인 경우 점수에 대한 A, B, C, D, F 등급을 출력하고,
# 범위에 해당하지 않으면 '입력 가능한 점수 범위는 0~100입니다.'를 출력하기.
# 점수에 대한 등급 판정은 if-elif-else 문을 이용하여 점수가 90~100일 때 A이고 10점 간격으로 B,C,D,F 등급이 결정된다.

score = int(input("점수 : "))

if score >= 0 and score <= 100:
    if score >= 90:
        degree = "A"
    elif score >= 80:
        degree = "B"
    elif score >= 70:
        degree = "C"
    elif score >= 60:
        degree = "D"
    else:
        degree = "F"
    print(score, ":", degree) # ex) 85 : B, 50 : F
else:
    print("입력 가능한 정수 범위는 0~100입니다.")