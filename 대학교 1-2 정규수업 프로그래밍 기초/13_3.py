outfile = open("C:/Users/DOR/Desktop/phones.txt","a",encoding="UTF8")
outfile.write("강감찬 010-1234-5681\n")
outfile.write("김유신 010-1234-5682\n")
outfile.write("정약용 010-1234-5683\n")
outfile.close()

infile = open("C:/Users/DOR/Desktop/script.txt","r",encoding="UTF8")

for line in infile:
    line = line.rstrip()
    word_list = line.split()
    for word in word_list:
        print(word)

infile.close()
