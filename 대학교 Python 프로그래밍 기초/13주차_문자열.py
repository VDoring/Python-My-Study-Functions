st = 'Text String'

# Included 출력됨
if 'x' in st:
    print('Included')
else:
    print('Not included')


print('length: ', len(st)) # length:  11 출력됨


st1 = '123'
st2 = '3.546'
print(st1, st2) # 123 3.546 출력됨


st3 = st.replace('S','s')
print(st3) # Text string 출력됨


st4 = 'TextString'
print(st.upper()) # TEXT STRING
print(st.lower()) # text string
print(st.isdigit(), st4.isdigit(), st1.isdigit()) # False False True -> 문자열이 숫자만으로 구성되었는지 검사
print(st.isalpha(), st4.isalpha(), st1.isalpha()) # False True False -> 문자열이 문자만으로 구성되었는지 검사
print(st.isalnum(), st4.isalnum(), st1.isalnum()) # False True True -> 문자열이 숫자/문자만으로 구성되었는지 검사