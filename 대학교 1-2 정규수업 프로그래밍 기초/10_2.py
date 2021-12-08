# dictionary 선언, 출력

bible = {'요한복음':256}
bible['시편'] = 50

print(bible)
for key in bible.keys():
    print(key, bible[key])

print(sorted(bible.keys())) # 정렬

for key in sorted(bible.keys()):
    print(key, bible[key])
