# 파일에 데이터 쓰기

outfile = open("output.txt", "w") # w -> 쓰기 모드

outfile.write("1111\n")
outfile.write("2222\n")
outfile.write("3333\n")

outfile.close()

# 1111
# 2222
# 3333
# 파일에 기록됨.