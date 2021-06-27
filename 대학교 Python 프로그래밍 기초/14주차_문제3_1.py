# ISBN 코드를 입력받을 때 - 문자를 판별할 수 있도록 만들어보기

...
isbn = input("ISBN 13자리(- 제외) : ")
if len(isbn) == 13 and not '-' in isbn: # isbn에 '-'가 포함되지 않으면 이란 조건 추가
    ...
b = "1234"
print(b[0], b[1], b[2], b[3])