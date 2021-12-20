import pickle

game_option = { "sound" : 8,
                "videoQ":"high",
                "money" : 100000,
                "weapon": ["gun", "sword"]}

file = open("save.p", "wb")

pickle.dump(game_option, file)

file.close()

file = open("save.p", "rb")

obj = pickle.load(file)

print(obj)

