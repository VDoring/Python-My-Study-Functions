# # 퀴즈 #3

# # 내 풀이
# url = input()
# url_non_http = url[7:] # naver.com
# url_com_pos = url_non_http.find('.com')
# url_non_http = url_non_http[:url_com_pos] # naver

# print(url_non_http[:3] + str(len(url_non_http)) + str(url_non_http.count('e')) + '!')



# 강사 풀이
url = 'http://naver.com'

my_str = url.replace('http://', '') # 규칙1. url 변수의 'http://' 부분을 ''로 바꾼다.
                                    # naver.com 출력됨

my_str = my_str[:my_str.index('.')] # 규칙2. my_str 변수에 있는 문자열에서 . 까지 자른다.
                                    # naver 출력됨

pw = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print('{0}의 비밀번호는 {1} 입니다.' .format(url,pw)) # nav51! 출력됨