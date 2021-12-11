# key = item 이름, value = 수량 
inventory = {}

# Todolist 1
# 1. 아이템 추가시 수량도 인자로 받음
# 2. inventory 전역함수이다. 인자로 받아서 처리하기
def add_item(item, amount, t_inventory):
    # 존재하면 1추가
    if check_item(item, t_inventory):
        t_inventory[item] += amount
        print(item+"의 수량은 "+str(t_inventory[item])+"입니다.")
    #존재하지않으면 추가하면서 수량은 1
    else:
        t_inventory[item] = amount
        print(item+"이 추가되었습니다.")

#기존의 수량을 모두 버림(수량 0)
#존재하지 않으면 무시
def remove_item(item, t_inventory):
    if check_item(item, t_inventory):
        t_inventory[item] = 0
        print(item+"의 수량이 0이 되었습니다.")
    else:
        print(item+"이 존재하지 않습니다.")
#새로운 함수, 포션 사용
#존재하는 아이템을 수량 1 빼기
def consume_item(item):
    pass


def check_item(item, t_inventory):
    return item in t_inventory

def print_menu():
    print("0. 끝내기")
    print("1. 아이템 추가")
    print("2. 아이템 삭제")
    print("3. 아이템 확인")
    print("4. 아이템 사용")

# Todolist 2
# while문을 아이템 다루기 함수로 구현
def use_item():
    while True:
        print_menu()
        option = int(input("메뉴 번호를 입력하세요)"))
        if option == 0:
            print("종료합니다.")
            break
        elif option == 1:
            new_item = input("아이템을 입력하세요.)")
            amount = int(input("수량을 입력하세요.)"))
            # Todolist 1'
            # 함수 인자 추가하는 기능 구현시 호출 부분 수정 필
            add_item(new_item, amount, inventory)
        elif option == 2:
            eliminated_item = input("아이템을 입력하세요.)")
            remove_item(eliminated_item, inventory)
        elif option == 3:
            print(inventory)
        elif option == 4:
            pass
        else:
            print("잘못된 번호를 입력하셨습니다.")


# todolist 3
# 캐릭터 만들기
# 캐릭터 이름으로 식별
# 캐릭터 인벤토리
# 캐릭터 장착기능









