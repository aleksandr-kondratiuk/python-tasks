x = int(input('Введите длину бассейна: '))
y = int(input('Введите ширину бассейна: '))

n = int(input('Введите расстоянии от одного из длинных бортиков: '))
m = int(input('Введите расстоянии от одного из коротких бортиков: '))

if x > y:
    if y > n and x > m:
        distance_to_x = n
        distance_to_y = m

        half_to_x = y / 2
        half_to_y = x / 2

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
    else:
        print('Вася должен быть в бассейне!')
else:
    print('Длина бассейна должна быть больше ширины!')