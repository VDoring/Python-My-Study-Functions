# 리스트에 append와 insert를 사용하여 인덱스 추가하기

letters = ['A', 'B', 'C', 'D', 'E', 'F']

letters.append("X")
print(letters) # ['A', 'B', 'C', 'D', 'E', 'F', 'X']

letters.insert(1, "X")
print(letters) # ['A', 'X', 'B', 'C', 'D', 'E', 'F', 'X']