inventory = []

def add_item(item):
	if item in inventory:
		print(item+"이 이미 존재합니다.")
	else:
		inventory.append(item)

add_item('힐링포션')
add_item('마나포션')
print(inventory)
