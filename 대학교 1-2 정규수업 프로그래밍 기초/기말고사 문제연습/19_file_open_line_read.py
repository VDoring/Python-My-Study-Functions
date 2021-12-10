# 파일 한 줄씩 읽기

infile = open("input.txt", "r") # r -> 읽기 모드
# 한글을 읽을 경우 open()에 encoding='UTF8'을 넣어야한다.

for line in infile:
    line = line.rstrip()
    print(line,'-')
    
infile.close()

# start -
# 1 -
# 2 -
# 3 -
# end -