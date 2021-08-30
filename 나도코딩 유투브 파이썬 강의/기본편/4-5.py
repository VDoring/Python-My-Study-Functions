# 탈출문자

# \n : 줄바꿈
print('고양이는 귀엽다.\n강아지는 멋지다.') # 두 줄에 걸쳐서 실행됨

# \" \' : 문장 내에서 " '(따옴표)
print("저는'user'입니다.") # 저는'user'입니다. 출력됨
print('저는"user"입니다.') # 저는"user"입니다. 출력됨
print("저는\"user\"입니다.") # 저는"user"입니다. 출력됨
print('저는\'user\'입니다.') # 저는'user'입니다. 출력됨

# \\ : 문장 내에서 \
print('C:\\Users\\DOR\\Desktop\\KRVG\\sff') # \를 문자 그대로 사용하기 위해선 \\를 사용해야한다.

# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine') # PineApple 출력됨
                         # Red Apple 출력후 커서를 맨 앞으로 옮기고 Pine을 출력한다.
                         # 결과적으로 Red부분은 Pine에 의해 덮어씌어지는것이다. (없어진다)

# \b : 백스페이스 (한 글자 삭제)
print('Redd\bApple') # RedApple 출력됨

# \t : Tab
print('Red\tApple') # Red     Apple 출력됨
