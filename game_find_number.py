import random

qnumber = random.randint(1, 50)
life = 6

while True:
    pnum = int(input("Введите возможное число:"))
    if qnumber < pnum:
        life -= 1
        print("Загаданное число меньше!\nОсталось жизней", life)
    elif qnumber > pnum:
        life -= 1
        print("Загаданное число больше!\nОсталось жизней", life)
    else:
        print("Вы победили!")
        break
    if life == 0:
        print("Вы проиграли!")
        break
