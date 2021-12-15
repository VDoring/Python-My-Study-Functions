infile = open("C:/Users/DOR/Desktop/phones.txt","r",encoding="UTF8")

lines = infile.read()
print(lines)

lines = infile.readlines()
print(lines)

for line in infile:
    print(line.rstrip()) # 한줄씩
infile.close()
