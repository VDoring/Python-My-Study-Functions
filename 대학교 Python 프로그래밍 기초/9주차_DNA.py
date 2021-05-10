def comp(seq):
    comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} # comp_dict 딕셔너리 선언
    seq_comp = "" # seq_comp 초기화
    for char in seq: # char의 값을 seq의 문자 순서대로 변경하며 반복
        seq_comp = seq_comp + comp_dict[char] # seq_comp에 comp_dict[char] 값 대입
                                              # for문에서 seq(입력값)에서 한글자씩 때어와 char에 저장한다.
                                              # 이후 이전에 저장된 데이터가 담겨있는 seq_comp와 comp_dict 딕셔너리에서 char 값을 찾는다.
    return seq_comp

def rev(seq):
    seq_rev = "".join(reversed(seq)) # seq의 문자열 값(사용자입력값)을 reverse하고,
                                     # 이 결과를 join()을 이용해 결합하여 seq_rev에 대입.
                                     # join()은 ['a','b']같은 리스트를 'ab'처럼 문자열로 합쳐서 반환해주는 함수이다.
    return seq_rev

def rev_comp(seq):
    tmp = comp(seq) # comp()를 사용한 다음
    return rev(tmp) # 거꾸로 바꾸어 반환한다.

src = input('DNA sequence: ')
cnvt = int(input("1(comp), 2(Rev), 3(Rev_Comp): "))
if cnvt >= 1 and cnvt <= 3:
    if cnvt == 1:
        rst = comp(src)
    elif cnvt == 2:
        rst = rev(src)
    else:
        rst = rev_comp(src)
    print(src, "->", rst) # 결과 출력
else: # 1,2,3 외 입력시
    print("1(comp), 2(Rev), 3(Rev_Comp)!!")