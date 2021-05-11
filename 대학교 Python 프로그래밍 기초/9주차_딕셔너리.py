dictionary = {'A':'X', 'B':'Y', 'C':'Z'}
# A를 언급하면 X를 반환. B를 언급하면 Y를 반환. C를 언급하면 Z를 반환한다.

print(dictionary) # {'A': 'X', 'B': 'Y', 'C': 'Z'} 출력됨
print(dictionary.keys()) # dict_keys(['A', 'B', 'C']) 출력됨
print(dictionary.values()) # dict_values(['X', 'Y', 'Z']) 출력됨

print(dictionary['B']) # Y 출력됨




english_dict = {}

english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'
print(english_dict) # {'one': '하나', 'two': '둘', 'three': '셋'} 출력됨

word = input('영어단어를 입력하세요: ') # two 입력시,
print(english_dict[word]) # 둘 출력됨

for key in english_dict: # 모든 키 값이 차례대로 출력된다.
    print(english_dict[key]) # 하나
                             # 둘
                             # 셋
                             # 출력됨