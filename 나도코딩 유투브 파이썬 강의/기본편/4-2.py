# 슬라이싱

jumin_number = "990120-1234567"

print('성별 : ' + jumin_number[7]) # 1 출력

print('연 : ' + jumin_number[0:2]) # 99 출력.
                                   # 0번째부터 1번째까지

print('월 : ' + jumin_number[2:4]) # 01 출력

print('일 : ' + jumin_number[4:6]) # 20 출력

print('생년월일 : ' + jumin_number[:6]) # 990120 출력
print('뒤 7자리수 : ' + jumin_number[7:]) # 1234567 출력
print('뒤 7자리수 (뒤에부터) : ' + jumin_number[-7:]) # 1234567 출력
                                                      # 0의 위치에서 -7만큼 이동하기