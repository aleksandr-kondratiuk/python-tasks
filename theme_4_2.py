# Вася плавал в бассейне размером x × y метров и устал.
# В этот момент он обнаружил, что находится на расстоянии n метров от одного
# из длинных бортиков (не обязательно от ближайшего) и m метров от одного из коротких
# бортиков.
# Какое минимальное расстояние должен проплыть
# Вася, чтобы выбраться из бассейна на бортик?
# Программа получает на вход числа x, y, n, m.
# Программа должна вывести число метров, которое нужно проплыть Васе до бортика.
# Перед решением задачи нарисуйте ее

x = int(input('Введите длину бассейна: '))
y = int(input('Введите ширину бассейна: '))

n = int(input('Введите расстоянии от одного из длинных бортиков: '))
m = int(input('Введите расстоянии от одного из коротких бортиков: '))

if x > y:
    if y > n and x > m:
        distance_to_x = n
        distance_to_y = m

        half_to_x = int(y / 2)
        half_to_y = int(x / 2)

        if half_to_x > distance_to_x:
            nearest_to_x = distance_to_x
        else:
            nearest_to_x = y - distance_to_x

        if half_to_y > distance_to_y:
            nearest_to_y = distance_to_y
        else:
            nearest_to_y = x - distance_to_y

        if nearest_to_x > nearest_to_y:
            print(nearest_to_y)
        else:
            print(nearest_to_x)

        print(distance_to_x, distance_to_y, half_to_x, half_to_y)
    else:
        print('Вася должен быть в бассейне!')
else:
    print('Длина бассейна должна быть больше ширины!')