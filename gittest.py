import pickle

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
def consume_item(item, t_inventory):
    if check_item(item, t_inventory):
        # 아이템의 수량이 0보다 큰가?
        if t_inventory[item] <= 0:
            print("현재 아이템의 수량이 적어서 사용할 수 없습니다.")
        else:
            t_inventory[item] -= 1
            print(item+"의 수량은 "+str(t_inventory[item])+"입니다.")
    else:
        print(item + "이 존재하지 않습니다.")


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
def use_item(inventory):
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
            c_item = input("사용할 아이템을 입력하세요.")
            consume_item(c_item, inventory)
        else:
            print("잘못된 번호를 입력하셨습니다.")


# key = item 이름, value = 수량 

# todolist 3
# 캐릭터 만들기
#inventory = {"base_inventory":b_inventory, "wearing_inventory":w_inventory}
# try 사용해 보기
#try:
#    load_file = open("game_save.p", "rb")
#    character = pickle.load(load_file)
#    load_file.close()
#    print("저장될 파일을 읽어왔습니다.")
#except:
#    print("읽어올 파일이 없습니다.")
#    character = {}
import os

if os.path.isfile("game_save1.p"):
    load_file = open("game_save1.p", "rb")
    character = pickle.load(load_file)
    load_file.close()
    print("저장된 파일을 읽어왔습니다.")
else:
    print("읽어올 파일이 없습니다.")
    character = {}

select_character = None
def new_character(name, t_character):
    if check_character(name, t_character):
        print("이미 존재하는 캐릭터의 이름입니다.")
    else:
        inventory = {}
        t_character[name] = inventory
        
def check_character(name, t_character):
    return name in t_character

def print_characterMenu():
    print("0. 저장하고 끝내기")
    print("1. 캐릭터 추가")
    print("2. 캐릭터 이름출력")
    print("3. 캐릭터 선택")
    print("4. 캐릭터 인벤토리 조작")
    
while True:
    print_characterMenu()
    option = int(input("메뉴를 선택해주세요.)"))
    if option == 0:
        save_file = open("game_save.p","wb")
        pickle.dump(character, save_file)
        save_file.close()
        print("게임 내용이 저장되었습니다")
        print("종료되었습니다.")
        break
    elif option == 1:
        name = input("캐릭터 이름을 입력하세요.)")
        new_character(name, character)
    elif option == 2:
        i = 1
        print("################")
        for name in character.keys():
            print(str(i)+". "+name)
            i += 1
        print("################")
    elif option == 3:
        temp_name = input("선택할 캐릭터의 이름을 입력해주세요.)")
        if check_character(temp_name, character):
            select_character = temp_name
            print(select_character + "이 선택되었습니다.")
        else:
            print(temp_name+"은 존재하지 않는 캐릭터입니다.")
    elif option == 4:
        if select_character == None:
            print("3번 메뉴로 캐릭터를 선택해주세요.")
        else:
            print("선택된 캐릭터는 "+select_character+" 입니다.")
            inventory = character[select_character]
            use_item(inventory)
    
# 캐릭터 이름으로 식별
# 캐릭터 인벤토리
# 캐릭터 장착기능









