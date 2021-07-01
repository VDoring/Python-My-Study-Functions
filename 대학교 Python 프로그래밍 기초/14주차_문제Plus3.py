c = 'a'
s = 'str'

print("#123456789#") #123456789#
print('#%c#'%c)      #a#
print('#%s#'%s)      #str#
print('#%9s#'%s)     #      str#
print('#%-9s#'%s)    #str      #

# 문자열 요소 개별 출력 버전
print("#%9c#"%s[0])  #        s#
print("#%-9c#"%s[1]) #t        #