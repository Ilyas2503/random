
import random

list_name = ["Asel", "Adilet", "ILyas", "Danislan"]
command1 = []
command2 = []
for n in range(len(list_name)):
    name = random.choice(list_name)
    if len(command1) <= int(len(list_name) / 2):
        command1.append(name)
        list_name.remove(name)
    else:
        command2.append(name)
        list_name.remove(name)
print(command1)
print(command2)
