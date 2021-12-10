# 항목이 리스트 안에 있는지 체크

computer = ["CPU", "RAM", "HDD", "SSD"]

if "CPU" in computer: # 체크
    computer.remove("CPU")
    
print(computer) # ['RAM', 'HDD', 'SSD']