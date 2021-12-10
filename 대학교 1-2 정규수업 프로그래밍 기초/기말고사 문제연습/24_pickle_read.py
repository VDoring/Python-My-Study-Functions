import pickle

file = open("colordata.p", "rb") # rb -> 바이너리 읽기모드

color = pickle.load(file)

print(color)

file.close()


# {'Dark': 10, 'Light': 50}