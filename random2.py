import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai",
         "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek",
         "Alymbek", "Dastan", "Maksat"]
command = []
for n in range(0, 13, 4):
    name = random.choice(names)
    if len(command) <= int(len(names) / 4):
        command.append(name)
        names.remove(name)
    else:
        command.append(name)
print(command)

