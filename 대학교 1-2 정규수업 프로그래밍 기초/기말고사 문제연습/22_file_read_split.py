infile = open("input.txt", "r") # r -> 읽기 모드

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word,'-')
        
infile.close()

# start -
# 1 -
# 2 -
# 3 -
# end -