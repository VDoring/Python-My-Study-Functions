# 파일을 읽기 모드로 열고 파일을 읽은 후 닫기

infile = open("input.txt", "r") # r -> 읽기 모드

lines = infile.read()
print(lines)

infile.close()

# start
# 1
# 2
# 3
# end
# 모든 내용을 출력한다.