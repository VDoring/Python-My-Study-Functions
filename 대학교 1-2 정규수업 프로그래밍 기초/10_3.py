# key = item 이름, value = 수량 
inventory = {}


def add_item(item):
    # 존재하면 1추가
    if check_item(item):
        inventory[item] += 1
        print(item+"의 수량은 "+str(inventory[item])+"입니다.")
    #존재하지않으면 추가하면서 수량은 1
    else:
        inventory[item] = 1
        print(item+"이 추가되었습니다.")

#기존의 수량을 모두 버림(수량 0)
#존재하지 않으면 무시
def remove_item(item):
    if check_item(item):
        inventory[item] = 0
        print(item+"의 수량이 0이 되었습니다.")
    else:
        print(item+"이 존재하지 않습니다.")
        
#새로운 함수, 포션 사용
#존재하는 아이템을 수량 1 빼기
def consume_item(item):
    if check_item(item): # 아이템이 딕셔너리에 존재할시
        if inventory[item] <= 0: # 아이템의 수량이 0일시
            print(item+"의 수량이 부족함")
        else: # 아이템의 수량이 1 이상일시
            inventory[item] -= 1
            print(item+"의 수량은 "+str(inventory[item])+"입니다.")
    else: # 아이템이 딕셔너리에 존재하지 않을시
        print(item+"이 존재하지 않습니다.")

def check_item(item):
    return item in inventory

def print_menu():
    print("0. 끝내기")
    print("1. 아이템 추가")
    print("2. 아이템 삭제")
    print("3. 아이템 확인")
    print("4. 아이템 사용")
    
while True:
    print_menu()
    option = int(input("메뉴 번호를 입력하세요)"))
    if option == 0:
        print("종료합니다.")
        break
    elif option == 1:
        new_item = input("아이템을 입력하세요.)")
        add_item(new_item)
    elif option == 2:
        eliminated_item = input("아이템을 입력하세요.)")
        remove_item(eliminated_item)
    elif option == 3:
        print(inventory)
    elif option == 4:
        use_item = input("> 아이템을 입력하세요.)")
        consume_item(use_item)
    else:
        print("잘못된 번호를 입력하셨습니다.")
