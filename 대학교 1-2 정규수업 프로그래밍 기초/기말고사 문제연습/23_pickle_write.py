import pickle

data = {"Dark":10, "Light":50}

file = open("colordata.p", "wb") # wb -> 바이너리 작성모드

pickle.dump(data, file) # 딕셔너리를 피클 파일에 저장

file.close()