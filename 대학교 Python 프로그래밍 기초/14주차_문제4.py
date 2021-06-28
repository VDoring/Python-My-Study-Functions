# 문자열을 입력받은 후, 만약 문자만으로 구성된 경우 모든 문자를 대문자로 변경하여 출력하고
# 숫자만으로 구성된 경우 문자열을 숫자로 변경한 후 +1을 하여 출력하기

st = input()
if st.isalpha(): # 문자만으로 구성되었을 경우
    st2 = st.upper() # 대문자 변경
    print(st2)
elif st.isdigit():
    n = int(st) + 1 # 정수 변환 후 +1
    print(n)